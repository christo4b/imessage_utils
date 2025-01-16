# mac_messages/exceptions.py
class MessageError(Exception):
    """Base exception for all message-related errors."""
    pass

class DeliveryError(MessageError):
    """Raised when message delivery fails."""
    pass

class ScriptError(MessageError):
    """Raised when AppleScript execution fails."""
    pass
