#!/usr/bin/env python3

__status__ = "Solution to Assignment Exercise 3"


def decide_rps(player1, player2):
    """
    This is to decide the result of a paper/rock/scissors match

    :param player1 and player2
    :return:
        Int: 0,1 and 2
             0: Tie
             1: Player1 wins
             2: Player2 wins
    :raises:
        TypeError if input is not a strong
        ValueError if players value passed do not have accepted values: "Rock", "Paper" or "Scissors"

    """

    if not (type(player1) is str) or not (type(player2) is str):
        raise TypeError("Invalid type passed as parameter")

    # Player one is the parent element, player is the child, and we map to the result.
    # Scissors: Scissors: 0
    #           Rock    : 2
    #           Paper   : 1
    # Rock      Scissors: 1
    #           Rock    : 0
    #           Paper   : 2
    #Paper      Scissors: 2
    #           Rock    : 1
    #           Paper   : 0

    # example: Player1(Rock), Player2 (Scissors), Player1 gets 1 point
    dict_play = {'Scissors':{'Scissors':0, 'Rock':2, 'Paper':1}, 'Rock':{'Scissors':1, 'Rock':0, 'Paper':2}, 'Paper':{'Scissors':2, 'Rock':1, 'Paper':0}}

    if (player1 in dict_play):
        temp_dict = dict_play[player1]
        if (player2 in temp_dict):
            return temp_dict[player2]
        else:
            # only acceptable values are Rock, Paper, Scissors
            raise ValueError("Player1 input is not in range")
    else:
        raise ValueError("Player2 input is not in range")

    # it should exit by this line.

    return 1



