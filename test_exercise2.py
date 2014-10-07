#!/usr/bin/env python3

""" Module to test exercise2.py """

# imports one per line
import pytest
from exercise2 import checksum


def test_checksum():
    """
        Inputs that are the correct format and length.
    """
    assert checksum("786936224306") is True
    assert checksum("085392132225") is True
    assert checksum("717951000842") is True
    assert checksum("085392132226") is False
    assert checksum("085392132227") is False
    assert checksum("717951000841") is False
    assert checksum("982636347284") is False


def test_input():
    """
        Inputs that are the incorrect format and length.
    """
    with pytest.raises(TypeError):
        checksum(1.0)

    with pytest.raises(TypeError):
        checksum(786936224306)

    with pytest.raises(TypeError):
        checksum(0.5)

    with pytest.raises(TypeError):
        checksum(4.5)


    with pytest.raises(ValueError):
        checksum("1")

    with pytest.raises(ValueError):
        checksum("1234567890")

    with pytest.raises(ValueError):
        checksum("38469")

    with pytest.raises(ValueError):
        checksum("21649200")

    with pytest.raises(ValueError):
        checksum("1")

    with pytest.raises(ValueError):
        checksum("1234567890")

    with pytest.raises(ValueError):
        checksum("1b34567890")

    with pytest.raises(ValueError):
        checksum("xdheuan123")

    with pytest.raises(ValueError):
        checksum("0000001c00")
