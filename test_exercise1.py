#!/usr/bin/env python3

""" Module to test exercise1.py """



# imports one per line
import pytest
from exercise1 import grade_to_gpa


def test_letter_grade():
    """
        Letter grade inputs
    """
    assert grade_to_gpa("A+") == 4.0
    assert grade_to_gpa("A") == 4.0
    assert grade_to_gpa("A-") == 3.7
    assert grade_to_gpa("B+") == 3.3
    assert grade_to_gpa("B") == 3
    assert grade_to_gpa("B-") == 2.7
    assert grade_to_gpa("FZ") == 0

    
    with pytest.raises(ValueError):
        grade_to_gpa("q")
        grade_to_gpa("aa")
        grade_to_gpa("j")
        grade_to_gpa("l")
        grade_to_gpa("o")
        grade_to_gpa("w+")
        grade_to_gpa("c-")
        grade_to_gpa("Z-")


def test_percentage_grade():
    """
        Numeric grade inputs
    """
    assert grade_to_gpa(100) == 4.0
    assert grade_to_gpa(95) == 4.0
    assert grade_to_gpa(90) == 4.0
    assert grade_to_gpa(89) == 4.0
    assert grade_to_gpa(87) == 4.0
    assert grade_to_gpa(85) == 4.0

    assert grade_to_gpa(84) == 3.7
    assert grade_to_gpa(82) == 3.7
    assert grade_to_gpa(80) == 3.7

    assert grade_to_gpa(79) == 3.3
    assert grade_to_gpa(78) == 3.3
    assert grade_to_gpa(77) == 3.3

    assert grade_to_gpa(76) == 3.0 
    assert grade_to_gpa(75) == 3.0
    assert grade_to_gpa(74) == 3.0
    assert grade_to_gpa(73) == 3.0

    assert grade_to_gpa(72) == 2.7
    assert grade_to_gpa(71) == 2.7
    assert grade_to_gpa(70) == 2.7

    assert grade_to_gpa(69) == 0.0
    assert grade_to_gpa(37) == 0.0
    assert grade_to_gpa(24) == 0.0
    assert grade_to_gpa(0) == 0.0
   




    with pytest.raises(ValueError):
        grade_to_gpa(101)

    with pytest.raises(ValueError):
        grade_to_gpa(-1)

    with pytest.raises(TypeError):
        grade_to_gpa(0.5)

    with pytest.raises(ValueError):
        grade_to_gpa(300)

    with pytest.raises(ValueError):
        grade_to_gpa(-50)

    with pytest.raises(TypeError):
        grade_to_gpa(-0.75)


def test_float_input():
    """
        Float inputs
    """
    with pytest.raises(TypeError):
        grade_to_gpa(82.5)

    with pytest.raises(TypeError):
        grade_to_gpa(79.9)

    with pytest.raises(TypeError):
        grade_to_gpa(0.4)

    with pytest.raises(TypeError):
        grade_to_gpa(99.9)

    with pytest.raises(TypeError):
        grade_to_gpa(59.9)


def test_cornercase_input():
    """
        Check Corner Testcases - Checking the cases that are right on the boundary.
    """
    assert grade_to_gpa(90) == 4.0
    assert grade_to_gpa(70) == 2.7
