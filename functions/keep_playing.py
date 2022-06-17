def keep_playing():
    '''returns true if the user wants to keep playing or false if not'''

    print()
    print("WRITE 'y' or 'yes' to continue playing or any other key to exit")
    answer = input("                   keep playing? (y) ").lower()
    if answer == "y" or answer == "yes":
        return True
    else:        
        return False
