def user_input(pos_north, pos_south, pos_west, pos_east) :
    valid_input = False
    while valid_input == False :
        uinput = input("Direction: ").upper()
        if uinput == "N" :
            if pos_north :
                break
        elif uinput == "A" :
            if pos_east :
                break
        elif uinput == "S" :
            if pos_south :
                break
        elif uinput == "W" :
            if pos_west :
                break
        else :
            print("Not a valid direction!")
    return uinput

print(user_input(True, False, False, True))            