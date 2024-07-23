#!/usr/bin/python3
"""
Module for validating UTF-8 encoding
"""


def validUTF8(data):
    """
    Determine if a given data set represents a valid UTF-8 encoding.

    :param data: List of integers representing bytes
    :return: True if data is a valid UTF-8 encoding, else False
    """
    num_bytes = 0

    for byte in data:
        # Check if the byte is greater than 255, which is invalid
        if byte > 255:
            return False

        # If no bytes are expected, check the current byte
        if num_bytes == 0:
            if (byte >> 5) == 0b110:
                num_bytes = 1
            elif (byte >> 4) == 0b1110:
                num_bytes = 2
            elif (byte >> 3) == 0b11110:
                num_bytes = 3
            elif (byte >> 7):
                return False
        else:
            # Check that the byte starts with '10'
            if (byte >> 6) != 0b10:
                return False
            num_bytes -= 1

    return num_bytes == 0


if __name__ == "__main__":
    data = [65]
    print(validUTF8(data))  # True

    data = [
        80, 121, 116, 104, 111, 110, 32, 105, 115, 32, 99, 111, 111, 108, 33
    ]
    print(validUTF8(data))  # True

    data = [229, 65, 127, 256]
    print(validUTF8(data))  # False
