from pynput import keyboard
import pyperclip
from syncv.network import send_clipboard_content
from syncv.storage import load_log


def on_copy(code):
    try:
        contents = pyperclip.paste()
        send_clipboard_content(code, contents)
    except Exception as e:
        print(f"Error in on_copy: {e}")

def on_paste():
    try:
        # keyboard.press_and_release('cmd+v')
        pyperclip.paste()
    except Exception as e:
        print(f"Error in on_paste: {e}")

def on_press(key, unique_code):
    try:
        if key == keyboard.Key.cmd:
            # pressed cmd; wait for c or v
            listener = keyboard.Listener(on_release=lambda k: on_release(k, unique_code))
            listener.start()
    except Exception as e:
        print(f'Error in on_press: {e}')

def on_release(key, unique_code):
    try:
        if key == keyboard.KeyCode.from_char('c'):
            on_copy(unique_code)
        elif key == keyboard.KeyCode.from_char('v'):
            on_paste()
        return False  # stop listener
    except Exception as e:
        print(f'Error in on_release: {e}')

def setup_hotkeys(unique_code):
    with keyboard.Listener(on_press=lambda k: on_press(k, unique_code)) as listener:
        listener.join()