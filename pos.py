def position(pos1, pos2):
    N,S,E,W = False

    if pos1 == 1 and pos2 == 1:
        N = True
        return N,S,E,W
    elif pos1 == 1 and pos2 == 2:
        N = True
        S = True
        E = True
        return N,S,E,W
    elif pos1 == 1 and pos2 == 3:
        S = True
        E = True
        return N,S,E,W
    elif pos1 == 2 and pos2 == 1:
        N = True
        return N,S,E,W
    elif pos1 == 2 and pos2 == 2:
        S = True
        W = True
        return N,S,E,W
    elif pos1 == 2 and pos2 == 3:
        E = True
        W = True
        return N,S,E,W
    elif pos1 == 3 and pos2 == 1:
        N = True
        return N,S,E,W
    elif pos1 == 3 and pos2 == 2:
        N = True
        S = True
        return N,S,E,W
    elif pos1 == 3 and pos2 == 3:
        S = True
        W = True
        return N,S,E,W
