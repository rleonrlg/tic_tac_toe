from math import fabs


def full_board(board):
    '''returns true if the board is complete or false if it's not'''

    if board[0] == " ":
        return False
    elif board[1] == " ":
        return False
    elif board[2] == " ":
        return False
    elif board[3] == " ":
        return False
    elif board[4] == " ":
        return False
    elif board[5] == " ":
        return False
    elif board[6] == " ":
        return False
    elif board[7] == " ":
        return False
    elif board[8] == " ":
        return False
    else:
        return True
    

            