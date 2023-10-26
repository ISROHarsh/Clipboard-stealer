## Prerequisites

Before running the script, you'll need to install the required Python libraries:

- `win32clipboard`: To access the Windows clipboard.
- `requests`: To send data to a Discord webhook.

You can install these libraries using `pip`:

```bash
pip install pywin32 requests
```

## Usage
1. Replace _'YOUR_DISCORD_WEBHOOK_URL'_ with your actual Discord webhook URL in the script.

2. Run the script. It will:
    - Hide the console window.
    - Add itself to the Windows startup (requires administrator rights).
    - Continuously monitor the clipboard for changes.
    - Send clipboard data to the configured Discord webhook.

## Important Notes

This script is for educational purposes only and should be used responsibly and ethically.
Unauthorized use for malicious purposes is illegal and unethical.

## License

This code is provided under an MIT License. See the [LICENSE](./LICENSE) file for details.