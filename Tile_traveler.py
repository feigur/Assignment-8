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
        