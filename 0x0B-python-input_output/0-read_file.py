#!/usr/bin/python3
"""Define read_file function"""


def read_file(filename=""):
    """Read a text file (UTF8) and prints it to stdout"""

    with open(filename, encoding="utf-8") as file:
        print(file.read(), end="")
