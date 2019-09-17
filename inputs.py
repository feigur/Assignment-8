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
    return possible_directions

    