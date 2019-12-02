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

 
def can_move(pos_north, pos_south, pos_west, pos_east, ) :
    possible_directions = ""
    if pos_north :
        possible_directions += " or (N)orth" 
    if pos_east :
        possible_directions += " or (E)ast" 
    if pos_south :
        possible_directions += " or (S)outh"
    if pos_west :
        possible_directions += " or (W)est" 

    possible_directions = "You can travel: " + possible_directions.replace(" or ", "", 1) + "."
    print(possible_directions)

          


def moves(pos, direction):
    vertical_index = 1
    horizontal_index = 0
    if direction == "N":
        if pos[vertical_index] + 1 < 4:
            pos[vertical_index] += 1
    if direction == "S":
        if pos[vertical_index] - 1 > 0:
            pos[vertical_index] -= 1
    if direction == "E":
        if pos[horizontal_index] + 1 < 4:
            pos[horizontal_index] += 1
    if direction == "W":
        if pos[horizontal_index] - 1 > 0:
            pos[horizontal_index] -= 1
    return pos, 

def position(pos, score, ):
    N = False
    S = False
    E = False
    W = False

    if pos == [1,1]:
        N = True
        can_move(N, S, W, E, )
        return user_input(N,S,W,E), score
    elif pos == [1,2]:
        N = True
        S = True
        E = True
        score = flip_lever(score)
        can_move(N, S, W, E, )
        return user_input(N,S,W,E), score
    elif pos == [1,3]:
        S = True
        E = True
        can_move(N, S, W, E, )
        return user_input(N,S,W,E), score
    elif pos == [2,1]:
        N = True
        can_move(N, S, W, E, )
        return user_input(N,S,W,E), score
    elif pos == [2,2]:
        S = True
        W = True
        score = flip_lever(score)
        can_move(N, S, W, E, )
        return user_input(N,S,W,E), score
    elif pos == [2,3]:
        E = True
        W = True
        score = flip_lever(score)
        can_move(N, S, W, E, )
        return user_input(N,S,W,E), score
    elif pos == [3,1]:
        N = True
        can_move(N, S, W, E, )
        return user_input(N,S,W,E), score
    elif pos == [3,2]:
        N = True
        S = True
        score = flip_lever(score)
        can_move(N, S, W, E, )
        return user_input(N,S,W,E), score
    elif pos == [3,3]:
        S = True
        W = True
        can_move(N, S, W, E, )
        return user_input(N,S,W,E), score
    
def flip_lever(score):
    y_n = input("Pull a lever (y/n): ")
    if y_n == "Y" or y_n == "y":
        score += 1
        print("You received 1 coin, your total is now {}.".format(score))
    if  y_n == "N" or y_n == "n":
        score = score
    return score

pos = [1,1]
score = 0
while True:
    direction, score = position(pos, score, )
    pos,  = moves(pos, direction)
    if pos == [3,1]:
        break
print("Victory! Total coins {}.".format(score))