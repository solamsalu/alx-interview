#!/usr/bin/python3
""" Task 0: UTF-8 validation """


def validUTF8(data):
    """ Variable to keep track of the number of continuation bytes expected
    """
    for i in data:
        if i < 0 or i >= 2**7:
            return False
        elif i >> 5 == 0b110:
            if len(data) < 2 or data[1] >> 6!= 0b10:
                return False
            data = data[2:]
        elif i >> 4 == 0b1110:
            if len(data) < 3 or data[1] >> 6!= 0b10 or data[2] >> 6!= 0b10:
                return False
            data = data[3:]
        elif i >> 3 == 0b11110:
            if len(data) < 4 or data[1] >> 6!= 0b10 or data[2] >> 6!= 0b10 or data[3] >> 6!= 0b10:
                return False
            data = data[4:]
        elif i >> 7 == 0:
            return False
        else:
            return False
    return True
