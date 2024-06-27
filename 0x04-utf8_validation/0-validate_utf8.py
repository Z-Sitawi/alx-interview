#!/usr/bin/python3
""" Module Doc """


def validUTF8(data):
    """ Determines if a given data set represents a valid UTF-8 encoding """
    # Number of bytes that follow a given lead byte
    num_bytes_to_follow = 0

    for num in data:
        # Check if the current byte is a continuation byte
        if num_bytes_to_follow > 0:
            # If the byte is not of the form 10xxxxxx, it's invalid
            if not (num & 0b11000000 == 0b10000000):
                return False
            num_bytes_to_follow -= 1
        else:
            # Determine the number of bytes that follow this lead byte
            if num & 0b10000000 == 0:
                num_bytes_to_follow = 0  # Single byte character
            elif num & 0b11100000 == 0b11000000:
                num_bytes_to_follow = 1  # Two byte character
            elif num & 0b11110000 == 0b11100000:
                num_bytes_to_follow = 2  # Three byte character
            elif num & 0b11111000 == 0b11110000:
                num_bytes_to_follow = 3  # Four byte character
            else:
                return False  # Invalid start byte

    # If we have any remaining bytes to follow, it means the data is incomplete
    return num_bytes_to_follow == 0
