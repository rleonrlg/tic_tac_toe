def present_2():
    '''return the chosen symbol of the user and the PC'''

    print("                    WELCOME TO")    
    print("                   TIC TAC TOE")
    print()
    print()
    print("                 start letter 'O'")
    print()
    print("                  Choose: O / X")
    print()
    print()

    symbol = ""
    while symbol != "O" and symbol != "X":
        symbol = input("            PLEASE SELECT LETTER 'O' or 'X'  ").upper()

    if symbol == "O":
        user = "O"
        pc = "X"
    else:
        user = "X"
        pc = "O"

    return user, pc