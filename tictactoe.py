"""
Tic Tac Toe Player
"""

import math
from re import S
import copy

X = "X"
O = "O"
EMPTY = None

def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if terminal(board):
        return EMPTY
    x = 0
    o = 0
    for list in board:
        for cell in list:
            if cell == X:
                x += 1
            elif cell == O:
                o += 1
    if x == o:
        return X
    return O
    
