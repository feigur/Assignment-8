def user_input(pos_north, pos_south, pos_west, pos_east) :
    """
    Takes in boolean vars for each direction, N, S, W, E. Asks user for an input and checks if it's valid
    Asks for another input if not valid. If valid, runs the movement function and moves the player.
    """
    valid_input = False
    while valid_input == False :
        uinput = input("Direction: ").upper()
        if uinput == "N" :
            if pos_north :
                return uinput
            else :
                print("Not a valid direction!")
        elif uinput == "E" :
            if pos_east :
                return uinput
            else :
                print("Not a valid direction!")
        elif uinput == "S" :
            if pos_south :
                return uinput
            else :
                print("Not a valid direction!")
        elif uinput == "W" :
            if pos_west :
                return uinput
            else :
                print("Not a valid direction!")
        else :
            print("Not a valid direction!")

print(user_input(True, False, False, True))            