#!/usr/bin/python3
""" A python module for utf-8 validation"""


def validUTF8(data):
    """ method for utf-8 validation"""

    one_byte_mask = 0b10000000
    two_byte_mask = 0b11100000
    three_byte_mask = 0b11110000
    four_byte_mask = 0b11111000
    continuation_mask = 0b11000000

    i = 0
    num_bytes = 0
    while i < len(data):
        byte = data[i]

        if (byte & one_byte_mask) == 0:
            num_bytes = 1
        elif (byte & two_byte_mask) == 0b11000000:
            num_bytes = 2
        elif (byte & three_byte_mask) == 0b11100000:
            num_bytes = 3
        elif (byte & four_byte_mask) == 0b11110000:
            num_bytes = 4
        else:
            return False

        if i + num_bytes > len(data):
            return False
        
        for j in range(1, num_bytes):
            if (data[i + j] & continuation_mask) != 0b10000000:
                return False

        i += num_bytes

    return True    
