#!/usr/bin/python3
"""Define append_write function"""


def append_write(filename="", text=""):
    """
    Append a string at the end of a text file (UTF8).

    Parametters
    -----------
    filename (str): File name.
    text (str): Text to write.

    Return: The number of characters added
    """

    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
