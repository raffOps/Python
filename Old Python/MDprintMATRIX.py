def printMATRIX(matrix):
    for x in matrix:
        print('\n')
        for y in x:
            print("%4d" % y, end=" ") ## -- end=" " -- evita quebra de linha automática