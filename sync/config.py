import os
import uuid

# 配置文件路径
CONFIG_FILE = os.path.expanduser("~/.sync_config")

def generate_unique_id():
    return str(uuid.uuid4())

def get_config():
    if not os.path.exists(CONFIG_FILE):
        unique_id = generate_unique_id()
        with open(CONFIG_FILE, "w") as f:
            f.write(unique_id)
        return unique_id
    with open(CONFIG_FILE, "r") as f:
        return f.read().strip()