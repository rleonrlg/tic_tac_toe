def winner (board, player):
    '''verify if there is three symbols y a row'''

    if  board[0] == board[1] == board[2] == player or \
        board[3] == board[4] == board[5] == player or \
        board[6] == board[7] == board[8] == player or \
        board[0] == board[3] == board[6] == player or \
        board[1] == board[4] == board[7] == player or \
        board[2] == board[5] == board[8] == player or \
        board[0] == board[4] == board[8] == player or \
        board[2] == board[4] == board[6] == player:
        return True
    else:
        return False