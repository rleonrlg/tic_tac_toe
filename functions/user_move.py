import imp
from functions.free_space import free_space
def user_move(board):
    '''returns the space chosen for the user'''

    positions = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    position = None
    while True:
        if position not in positions:
            position = input("your turn, chose an empty space from 1 to 9: ")
        else:
            position = int(position)
            if not free_space(board, position-1):
                print("the space you have chose has already been taken")
            else:
                return position-1
                