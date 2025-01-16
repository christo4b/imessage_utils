import pytest
from unittest.mock import patch, mock_open
from mac_messages.sender import MessageSender
from mac_messages.exceptions import ScriptError

@pytest.fixture
def sender():
    return MessageSender()

def test_run_applescript_success(sender):
    script = 'tell application "Messages" to return "test"'
    with patch('builtins.open', mock_open()), \
         patch('os.popen') as mock_popen, \
         patch('os.path.exists', return_value=True), \
         patch('os.remove'):
        mock_popen.return_value.read.return_value = "success"
        success, result = sender._run_applescript(script)
        assert success
        assert result == "success"

def test_run_applescript_error(sender):
    script = 'invalid script'
    with patch('builtins.open', mock_open()), \
         patch('os.popen') as mock_popen, \
         patch('os.path.exists', return_value=True), \
         patch('os.remove'):
        mock_popen.return_value.read.return_value = "error: Invalid script"
        success, result = sender._run_applescript(script)
        assert not success
        assert "error" in result

@pytest.mark.parametrize("method,expected_script_type", [
    ('send_imessage', 'iMessage'),
    ('send_sms', 'SMS'),
])
def test_send_methods(sender, method, expected_script_type):
    with patch.object(sender, '_run_applescript', return_value=(True, "success")):
        send_func = getattr(sender, method)
        assert send_func("1234567890", "Test message")

def test_send_fallback_to_sms(sender):
    with patch.object(sender, 'send_imessage', return_value=False), \
         patch.object(sender, 'send_sms', return_value=True):
        assert sender.send("1234567890", "Test message")
