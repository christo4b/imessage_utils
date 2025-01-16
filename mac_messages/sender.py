import os
import logging
from time import sleep
from typing import Tuple
from .exceptions import MessageError, DeliveryError, ScriptError
from .scripts import IMESSAGE_SEND, SMS_SEND, CHECK_STATUS

logger = logging.getLogger(__name__)

class MessageSender:
    """Handles sending messages via iMessage and SMS on macOS."""

    def __init__(self, script_path: str = '/tmp/message.applescript'):
        self.script_path = script_path

    def _run_applescript(self, script: str) -> Tuple[bool, str]:
        """Execute AppleScript and return success status and result."""
        try:
            with open(self.script_path, 'w') as f:
                f.write(script)
            result = os.popen(f'osascript {self.script_path}').read().strip()
            if 'error:' in result:
                raise ScriptError(result)
            return True, result
        except Exception as e:
            return False, str(e)
        finally:
            if os.path.exists(self.script_path):
                os.remove(self.script_path)

    def check_message_status(self, phone: str, msg: str) -> bool:
        """Check if a specific message was delivered to a recipient."""
        success, result = self._run_applescript(
            CHECK_STATUS.format(phone=phone, msg=msg)
        )
        return success and "delivered" in result

    def send_imessage(self, phone: str, msg: str) -> bool:
        """Send message via iMessage."""
        success, result = self._run_applescript(
            IMESSAGE_SEND.format(phone=phone, msg=msg)
        )
        return success and "success" in result

    def send_sms(self, phone: str, msg: str) -> bool:
        """Send message via SMS."""
        success, result = self._run_applescript(
            SMS_SEND.format(phone=phone, msg=msg)
        )
        return success and "success" in result

    def send(self, phone: str, msg: str) -> bool:
        """Send message, trying iMessage first then SMS if needed."""
        logger.info(f"Attempting to send message to {phone}")

        if self.send_imessage(phone, msg):
            sleep(2)  # Wait for delivery status
            if self.check_message_status(phone, msg):
                logger.info("iMessage delivered successfully")
                return True
            logger.info("iMessage failed to deliver, trying SMS...")
        else:
            logger.info("iMessage send failed, trying SMS...")

        if self.send_sms(phone, msg):
            logger.info("SMS sent successfully")
            return True

        logger.error("All message attempts failed")
        return False

def send_message(phone: str, msg: str) -> bool:
    """Convenience function to send a message."""
    sender = MessageSender()
    return sender.send(phone, msg)