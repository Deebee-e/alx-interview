#!/usr/bin/python3
"""
Determines if a given data set represents a valid UTF-8 encoding
"""


def validUTF8(data):
    """
    Validates UTF-8 encoding

    Args:
        data (list): A dataset represented by a list of integers

    Return:
        True if data is a valid UTF-8 encoding, else False
    """

    byte_count = 0

    for byte in data:
        if byte_count == 0:
            if (byte >> 7) == 0b0:
                # Single byte character, no need for further checks
                continue
            elif (byte >> 5) == 0b110:
                byte_count = 1
            elif (byte >> 4) == 0b1110:
                byte_count = 2
            elif (byte >> 3) == 0b11110:
                byte_count = 3
            else:
                return False
        else:
            if (byte >> 6) != 0b10:
                return False
            byte_count -= 1

    return byte_count == 0
