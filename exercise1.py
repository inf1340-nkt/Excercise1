#!/usr/bin/env python3

""" Assignment 1, Exercise 1, INF1340, Fall, 2014. Grade to gpa conversion

This module contains one function grade_to_gpa. It can be passed a parameter
that is an integer (0-100) or a letter grade (A+, A, A-, B+, B, B-, or FZ). All
other inputs will result in an error.

Example:
    $ python exercise1.py

"""

__status__ = "Solution to Assignment Exercise 1"

# imports one per line

def grade_to_gpa(grade):
    """
    Returns the UofT Graduate GPA for a given grade.

    :param:
        grade (integer or string): Grade to be converted
            If integer, accepted values are 0-100.
            If string, accepted values are A+, A, A-, B+, B, B-, FZ

    :return:
        float: The equivalent GPA
            Value is 0.0-4.0

    :raises:
        TypeError if parameter is not a string or integer
        ValueError if parameter is out of range
    """

    letter_grade = ""
    gpa = 0.0

    # dictionary to map letters to GPA.
    # letters corresponds to a number, 4 being the highest value

    dic_letter = {'A+': 4, 'A': 4, 'A-': 3.7, 'B+': 3.3, 'B': 3, 'B-': 2.7, 'FZ': 0}

    # dict to map range in grades to its corresponding GPA
    # grade range is in a format of lowest to highest, example: 90, lowest to 100, highest
    # grade between the range of lowest and highest receives a number as GPA
    # example: grade 73 results in the GPA of 3.3
    dic_num = {(90,100): 4, (85,89): 4, (80,84): 3.7, (77,79): 3.3, (73,76): 3, (70,72): 2.7, (0,69): 0}

    if type(grade) is str:
        # check that the grade is one of the accepted values
        # assign grade to letter_grade
        if( grade in dic_letter):
            return dic_letter[grade]

        # If not found in the dictionary, it is out of range

        raise ValueError("Mark specified in letter is not in range not in range")
        #return 'ERROR: Mark specified in letter is not in range not in range'

    elif type(grade) is int:

        # check that grade is in the accepted range
        # convert the numeric grade to a letter grade
        # assign the value to letter_grade
        # key[0] is the lower bound
        # key[1] is the upper bound
        # grade is in between

        for key, value in dic_num.items():
            if(grade >= key[0] and grade < (key[1] + 1)):
                return value

        # if not found in the dictionary, then must of out of range
        raise ValueError("Mark specified in number is not in range")
        #return 'ERROR: Mark specified in number is not in range'

    else:
        # raise a TypeError exception
        raise TypeError("Invalid type passed as parameter")

    # This section is not required and won't be executed.
    if letter_grade == "A":
        gpa = 4.0

    return gpa

