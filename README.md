# imessage_utils

A Python package for sending messages through the macOS Messages app.

## Features

- Send iMessages and SMS
- Automatic fallback from iMessage to SMS
- Delivery status checking
- Comprehensive error handling

## Installation

```bash
pip install imessage_utils
```

## Usage

```python
from mac_messages import send_message

# Simple usage
success = send_message("+1234567890", "Hello!")

# Advanced usage
from mac_messages import MessageSender

sender = MessageSender()
if sender.send_imessage("+1234567890", "Hello via iMessage!"):
    print("iMessage sent successfully")
```

## Requirements

- macOS with Messages app configured
- Python 3.7+

## Development

1. Clone the repository
2. Install development dependencies: `pip install -r requirements.txt`
3. Run tests: `pytest tests/`

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.
