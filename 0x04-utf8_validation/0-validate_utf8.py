#!/usr/bin/python3
"""
Determines if a given data set represents a valid UTF-8 encoding
"""

def validUTF8(data):
    """
    Validates UTF-8 encoding.

    Args:
        data (list): A dataset represented by a list of integers.

    Returns:
        bool: True if data is a valid UTF-8 encoding, else False.
    """

    byte_count = 0

    for num in data:
        byte = num & 0xFF  # Ensure we're only considering the last 8 bits

        if byte_count == 0:
            if (byte >> 7) == 0b0:
                # Single byte character (0xxxxxxx) is valid
                continue
            elif (byte >> 5) == 0b110:
                byte_count = 1  # 2-byte character (110xxxxx)
            elif (byte >> 4) == 0b1110:
                byte_count = 2  # 3-byte character (1110xxxx)
            elif (byte >> 3) == 0b11110:
                byte_count = 3  # 4-byte character (11110xxx)
            else:
                return False  # Invalid starting byte
        else:
            if (byte >> 6) != 0b10:
                return False  # Invalid continuation byte (10xxxxxx)
            byte_count -= 1

    return byte_count == 0  # Ensure all characters are fully processed

