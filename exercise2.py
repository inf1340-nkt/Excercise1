#!/usr/bin/env python3

"""
    Perform a checksum on a UPC

    Assignment 1, Exercise 2, INF1340 Fall 2014
"""

__status__ = "Solution to Assignment Exercise 2"

# imports one per line


def checksum (upc):
    """
    Checks if the digits in a UPC is consistent with checksum

    :param upc: a 12-digit universal product code
    :return:
        Boolean: True, checksum is correct
        False, otherwise
    :raises:
        TypeError if input is not a strong
        ValueError if string is the wrong length (with error string stating how many digits are over or under
    """

    # check type of input
    # raise TypeError if not string

    # xxxxxxxxxxx    x
    # check length of string
    # raise ValueError if not 12

    # convert string to array
    # generate checksum using the first 11 digits provided
    # check against the the twelfth digit
    # result of first 11 digits must be consistent with the value of the 12th digit
    # value must be number

    # return True if they are equal, False otherwise
    num = []
    #"123456"  --> "1" "2" "3" "4" "5" "6" --> num = [1,2,3,4,5,6] --> num[0] = 1, num[3] = 4
    if type(upc) is str:
        for i in range(0, len(upc)):
            try:
                num.append(int(upc[i]))
            except ValueError:
                raise ValueError("Not correct length")
            # if upc[i] is not number  checksum('1b2')
    else:
        raise TypeError("Invalid type passed as parameter")
        #raiseError

    if len(num) != 12:
        raise ValueError("Not correct length")


    odd, even =  num[::2], num[1::2]
    result = 0
    for i in range(0,len(odd)):
        result = result + odd[i]

    result *= 3

    # This is to add even numbered digits
    for i in range(0, (len(even)-1)):
        result = result + even[i]

    result %= 10
    if result != 0:
        result = 10 - result

    if result == num[11]:
        return True

    return False

