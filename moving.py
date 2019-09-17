pos[][] = "" 
for i in range(0,3) :
    for j in range(0,3) :
        pos[i][j] = str(i+1) + "," + str(j+1)   

for i in range(0,3) :
    for j in range(0,3) :
        print(pos[i][j])