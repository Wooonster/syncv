import argparse
import os
import requests
from .config import get_config
from .storage import save_to_log, read_log, clear_log
from .clipboard import copy_to_clipboard, paste_from_clipboard

SERVER_URL = "http://localhost:5000"

def init():
    unique_id = get_config()
    print(f"Initialization complete. Your unique ID is: {unique_id}")

def copy():
    # content = paste_from_clipboard()
    # response = requests.post(f"{SERVER_URL}/copy", json={"content": content})
    # if response.status_code == 200:
    #     save_to_log(content)
    #     print("Content copied and synced.")
    # else:
    #     print("Failed to sync content.")
    print('ah, ah, not yet')

def paste():
    # response = requests.get(f"{SERVER_URL}/paste")
    # if response.status_code == 200:
    #     clipboard_data = response.json().get("clipboard", [])
    #     if clipboard_data:
    #         content = clipboard_data[-1]
    #         copy_to_clipboard(content)
    #         print("Content pasted to clipboard.")
    #     else:
    #         print("Clipboard is empty.")
    # else:
    #     print("Failed to fetch content.")
    print('ah, ah, not yet')


def list_clipboard():
    # log = read_log()
    # print("Clipboard history:")
    # for line in log:
    #     print(line.strip())
    print('ah, ah, not yet')


def clear():
    # requests.post(f"{SERVER_URL}/clear")
    # clear_log()
    # print("Clipboard cleared.")
    print('ah, ah, not yet')


def main():
    parser = argparse.ArgumentParser(description="SyncV - Cross-OS Clipboard Tool")
    parser.add_argument("command", choices=["init", "copy", "paste", "list", "clear"], help="Command to execute")
    args = parser.parse_args()

    if args.command == "init":
        init()
    elif args.command == "copy":
        copy()
    elif args.command == "paste":
        paste()
    elif args.command == "list":
        list_clipboard()
    elif args.command == "clear":
        clear()