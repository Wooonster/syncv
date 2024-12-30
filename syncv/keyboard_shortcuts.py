import os
import sys
import threading
import pyperclip
import platform

try:
    from pynput import keyboard  # Import for GUI environments
except ImportError:
    keyboard = None  # Fallback if GUI dependencies are not available

from syncv.network import send_clipboard_content


def is_headless():
    """Detect if the environment is headless."""
    return os.environ.get("DISPLAY") is None and os.environ.get("WAYLAND_DISPLAY") is None


def get_os():
    """Return the current operating system."""
    return platform.system().lower()


def on_copy(unique_code):
    """Handle copy action."""
    try:
        contents = pyperclip.paste()
        send_clipboard_content(unique_code, contents)
        print(f"Copied: {contents}")
    except Exception as e:
        print(f"Error in on_copy: {e}")


def on_paste():
    """Handle paste action."""
    try:
        # Simulate paste operation
        print("Paste triggered.")
        pyperclip.paste()
    except Exception as e:
        print(f"Error in on_paste: {e}")


def monitor_clipboard(unique_code):
    """Poll clipboard changes in headless environments."""
    previous_content = pyperclip.paste()
    print("Starting clipboard monitor for all environments...")
    while True:
        try:
            current_content = pyperclip.paste()
            if current_content != previous_content:
                previous_content = current_content
                send_clipboard_content(unique_code, current_content)
                print(f"Clipboard updated: {current_content}")
        except Exception as e:
            print(f"Error monitoring clipboard: {e}")


def on_press(key, unique_code):
    """Handle key press for GUI environments."""
    try:
        if hasattr(key, 'char') and key.char in ('c', 'v'):
            if key.char == 'c':
                on_copy(unique_code)
            elif key.char == 'v':
                on_paste()
    except Exception as e:
        print(f"Error in on_press: {e}")


def setup_hotkeys(unique_code):
    """Setup hotkeys or clipboard monitoring for all environments."""
    os_name = get_os()
    print(f"Detected OS: {os_name}")

    # Fallback for headless environments
    if is_headless():
        print("Headless mode detected. Using clipboard monitoring.")
        monitor_clipboard(unique_code)
        return

    # GUI Environment: Hotkey setup
    if keyboard:
        print("GUI environment detected. Setting up hotkeys.")
        try:
            def on_key_release(key):
                on_press(key, unique_code)

            with keyboard.Listener(on_release=on_key_release) as listener:
                listener.join()
        except Exception as e:
            print(f"Error setting up hotkeys: {e}")
    else:
        # Headless fallback even in GUI OS if `pynput` is unavailable
        print("Fallback to clipboard monitoring due to missing GUI dependencies.")
        monitor_clipboard(unique_code)