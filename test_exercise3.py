#!/usr/bin/env python3

import pytest
from exercise3 import decide_rps


def test_checksum():
    """
        Inputs that are the correct format and length
    """
    assert decide_rps("Rock", "Paper") == 2
    assert decide_rps("Scissors", "Scissors") == 0
    assert decide_rps("Rock", "Scissors") == 1
    assert decide_rps("Paper", "Rock") == 1
    assert decide_rps("Paper", "Paper") == 0
    assert decide_rps("Scissors", "Paper") == 1
    assert decide_rps("Rock", "Rock") == 0
    assert decide_rps("Scissors", "Rock") == 2
    assert decide_rps("Paper", "Scissors") == 2


def test_input():
    """
        Inputs are of correct type
    """

    # Invalid Type Error
    with pytest.raises(TypeError):
        decide_rps(1, "Scissors")

    with pytest.raises(TypeError):
        decide_rps("Rock", 5.5)

    with pytest.raises(TypeError):
        decide_rps(0.5, "Paper")

    with pytest.raises(TypeError):
        decide_rps(1.2, 5.4)

    with pytest.raises(TypeError):
        decide_rps("Rock", -1)

    # Problem with Player 1 input
    with pytest.raises(ValueError):
        decide_rps("Rockk", "Paper")

    with pytest.raises(ValueError):
        decide_rps("Scissorss", "Scissors")

    with pytest.raises(ValueError):
        decide_rps("stone", "knife")

    with pytest.raises(ValueError):
        decide_rps("Papier", "rock")

    with pytest.raises(ValueError):
        decide_rps("Rook", "paper")



    # Problem with Player 2 input
    with pytest.raises(ValueError):
        decide_rps("Scissors", "Door")

    with pytest.raises(ValueError):
        decide_rps("Paper", "5.2")

    with pytest.raises(ValueError):
        decide_rps(0.25, "Rock")

    with pytest.raises(ValueError):
        decide_rps("Papier", "Rox")

    with pytest.raises(ValueError):
        decide_rps(-1, "Stone")



