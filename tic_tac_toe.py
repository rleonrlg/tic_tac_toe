import random
import time
import os


from functions.screen_2 import present_2
from functions.show_booar import show_board
from functions.keep_playing import keep_playing
from functions.winner import winner
from functions.full_board import full_board
from functions.free_space import free_space
from functions.user_move import user_move


def mov_pc_hard(board, pc, user):
    for i in range(9):
        copy = list(board)
        if free_space(copy, i):
            copy[i] = pc
            if winner(copy, pc):
                return i                           
                          
    for i in range(9):
        copy = list(board)
        if free_space(copy, i):
            copy[i] = user
            if winner(copy, user):
                return i
    if pc == "X":
        if board[4] == " ":
            return 4
        else:
            empty_courner = []
            for i in [0, 2, 6, 8]:
                if free_space(board, i):
                    empty_courner.append(i)
            empty_spaces = []
            for i in [1, 3, 5 ,7]:
                if free_space(board, i):
                    empty_spaces.append(i)
                    if len(empty_courner) <= 0:
                        return random.choice(empty_courner)
                    else:
                        return random.choice(empty_spaces)
    if pc == "O":
        num = 0
        for i in range(9):
            if free_space(board, i):
                num += 1
            if num == 7:
                if board[4] == " ":
                    return 4
    while True:
        space = random.randint(0,8)
        if not free_space(board, space):
            space = random.randint(0,8)
        else:
            return space



playing = True
while playing:
    board = [" "] * 9
    os.system("cls")    
    user, pc = present_2()
    os.system("cls")
    show_board(board)
    if user == "O":
        turn = "user"
    else:
        turn = "PC"

    game = True
    while game:
        if full_board(board):
            print("            TIE")
            game = False            
        elif turn == "user":
            space = user_move(board)
            board[space] = user
            turn = "PC"
            os.system("cls")
            show_board(board)
            if winner(board, user):
                print("            YOU WIN")
                game = False
        elif turn == "PC":
            print("            I'M thinking")
            time.sleep(2)            
            space = mov_pc_hard(board, pc, user)
            board[space] = pc
            turn = "user"
            os.system("cls")
            show_board(board)
            if winner(board, pc):
                print("            YOU LOOSE")
                game = False
    
    playing = keep_playing()
    