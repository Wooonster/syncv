from setuptools import setup, find_packages

setup(
    name="syncv",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "flask",
        "pyperclip",
        "requests",
        "argparse",
    ],
    entry_points={
        "console_scripts": [
            "syncv=clipboard_sync.main:main",
        ],
    },
)