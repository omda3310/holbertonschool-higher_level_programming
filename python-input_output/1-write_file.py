#!/usr/bin/python3
"""a function that appends a string at the end of a text file (UTF8)
and returns the number of characters added"""


def append_write(filename="", text=""):
    """This function has two parameters: filename is the name of file and
    text is the string to be writing in the text"""

    with open(filename, 'w', encoding='utf-8') as filename:

        """This function uses the with open method to open the file in writing mode(mode='w')
        and utf-8 encoding(mode='utf-8')"""

        return filename.write(text)
