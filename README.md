# imessage_utils

A Python package for sending messages through the macOS Messages app.

## Features

- Send iMessages and SMS
- Automatic fallback from iMessage to SMS
- Delivery status checking
- Comprehensive error handling

## Installation

```bash
pip install mac-messages
```

## Usage

### Python API
```python
from mac_messages import MessageSender

sender = MessageSender()

# Try iMessage with SMS fallback
success = sender.send("+1234567890", "Hello!")

# SMS only
success = sender.send_sms("+1234567890", "Hello via SMS!")

# iMessage only
success = sender.send_imessage("+1234567890", "Hello via iMessage!")
```

### Command Line
```bash
# Install locally
pip install -e .

# Normal send (tries iMessage, falls back to SMS)
python test_usage.py "+1234567890" "Hello world"

# SMS only
python test_usage.py --sms-only "+1234567890" "Hello via SMS"

# iMessage only
python test_usage.py --imessage-only "+1234567890" "Hello via iMessage"
```

## Requirements

- macOS with Messages app configured
- Python 3.7+

## Development

1. Clone the repository
2. Install development dependencies: `pip install -r requirements.txt`
3. Run tests: `pytest tests/`

## License

MIT License