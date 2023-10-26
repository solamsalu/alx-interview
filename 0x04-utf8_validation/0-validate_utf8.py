#!/usr/bin/python3
""" Task 0: UTF-8 validation """


def validUTF8(data):
    """ Variable to keep track of the number of continuation bytes expected
    """
    num_continuation_bytes = 0

    for byte in data:
        """ Check if it is a continuation byte """
        if num_continuation_bytes > 0 and (byte >> 6) == 0b10:
            num_continuation_bytes -= 1
        elif num_continuation_bytes == 0:
            if (byte >> 7) == 0b0:
                num_continuation_bytes = 0
            elif (byte >> 5) == 0b110:
                num_continuation_bytes = 1
            elif (byte >> 4) == 0b1110:
                num_continuation_bytes = 2
            elif (byte >> 3) == 0b11110:
                num_continuation_bytes = 3
            else:
                return False
        else:
            return False
   
    return True
