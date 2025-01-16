import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent.parent))

from imessage_utils.scripts import IMESSAGE_SEND, SMS_SEND, CHECK_STATUS

def test_script_formatting():
    phone = "1234567890"
    msg = "Test message"

    for script in [IMESSAGE_SEND, SMS_SEND, CHECK_STATUS]:
        formatted = script.format(phone=phone, msg=msg)
        assert f'buddy "{phone}"' in formatted
        assert f'"{msg}"' in formatted