#!/usr/bin/python3

def validUTF8(data):
    num_bytes = 0  # Number of bytes expected in the current character

    for num in data:
        # Mask the number to get the last 8 bits
        byte = num & 0xFF
        # Determine the number of bytes expected
        if num_bytes == 0:
            if (byte >> 7) == 0b0:  # 0xxxxxxx
                num_bytes = 0
            elif (byte >> 5) == 0b110:  # 110xxxxx
                num_bytes = 1
            elif (byte >> 4) == 0b1110:  # 1110xxxx
                num_bytes = 2
            elif (byte >> 3) == 0b11110:  # 11110xxx
                num_bytes = 3
            else:
                return False  # Invalid starting byte
        else:
            # Check continuation byte (10xxxxxx)
            if (byte >> 6) != 0b10:
                return False  # Invalid continuation byte
            num_bytes -= 1

    # If we are still expecting bytes after processing all data, it's invalid
    return num_bytes == 0
