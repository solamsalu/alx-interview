#!/usr/bin/python3

"""  
Task 0: UTF-8 validation 
"""


def validUTF8(data):
    """ Variable to keep track of the number of 
    continuation bytes expected """

    count = 0
    for num in data:
        # Ensure the number is within the valid range for a byte
        if not 0 <= num < 256:
            return False

        # If we're expecting continuation bytes, check if this byte is one
        if count > 0:
            if (num >> 6) != 0b10:
                return False
            count -= 1
            continue

        # If this is a new character, determine its length based on the MSBs
        if (num >> 5) == 0b110:
            count = 1
        elif (num >> 4) == 0b1110:
            count = 2
        elif (num >> 3) == 0b11110:
            count = 3
        elif (num >> 7) == 1:  # Single-byte characters must start with `0`
            return False

    # If we're still expecting continuation bytes, the data is invalid
    return count == 0
