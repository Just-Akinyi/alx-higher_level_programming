#!/usr/bin/python3
"""Define write_file function"""


def write_file(filename="", text=""):
    """
    Write a string to a text file (UTF8).

    Parametters
    -----------
    filename (str): File name.
    text (str): Text to write.

    Returns: The number of characters written.
    """

    with open(filename, "w", encoding="utf-8") as file:
        return file.write(text)
