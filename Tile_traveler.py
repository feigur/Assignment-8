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

 
def can_move(pos_north, pos_south, pos_west, pos_east) :
    possible_directions = ""
    if pos_north :
        possible_directions += " or (N)orth" 
    if pos_west :
        possible_directions += " or (W)est" 
    if pos_east :
        possible_directions += " or (E)ast" 
    if pos_south :
        possible_directions += " or (S)outh"
    possible_directions = "You can travel: " + possible_directions.replace(" or ", "", 1) + "."
    print(possible_directions)

          


def moves(pos1,pos2,direction):
    if direction == "N":
        if pos1+1 < 4:
            pos1 += 1
    if direction == "S":
        if pos1-1 > 0:
            pos1 -= 1
    if direction == "E":
        if pos2+1 < 4:
            pos2 += 1
    if direction == "W":
        if pos2-1 > 0:
            pos2 -= 1
    return pos1, pos2
def position(pos1, pos2):
    N = False
    S = False
    E = False
    W = False

    if pos1 == 1 and pos2 == 1:
        N = True
        can_move(N,S,W,E)
        return user_input(N,S,W,E)
    elif pos1 == 1 and pos2 == 2:
        N = True
        S = True
        E = True
        can_move(N,S,W,E)
        return user_input(N,S,W,E)
    elif pos1 == 1 and pos2 == 3:
        S = True
        E = True
        can_move(N,S,W,E)
        return user_input(N,S,W,E)
    elif pos1 == 2 and pos2 == 1:
        N = True
        can_move(N,S,W,E)
        return user_input(N,S,W,E)
    elif pos1 == 2 and pos2 == 2:
        S = True
        W = True
        can_move(N,S,W,E)
        return user_input(N,S,W,E)
    elif pos1 == 2 and pos2 == 3:
        E = True
        W = True
        can_move(N,S,W,E)
        return user_input(N,S,W,E)
    elif pos1 == 3 and pos2 == 1:
        N = True
        can_move(N,S,W,E)
        return user_input(N,S,W,E)
    elif pos1 == 3  and pos2 == 2:
        N = True
        S = True
        can_move(N,S,W,E)
        return user_input(N,S,W,E)
    elif pos1 == 3 and pos2 == 3:
        S = True
        W = True
        can_move(N,S,W,E)
        return user_input(N,S,W,E)

pos1 = 1
pos2 = 1
while True:
    direction= position(pos1,pos2)
    pos2,pos1 = moves(pos2,pos1,direction)
    if pos1 == 3 and pos2 == 1:
        break
print("Victory!")