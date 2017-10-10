# O nome das variáveis a,b e c devem ser definidos no programa main
def printDATABASE(arquivo, *args):
    file = open(arquivo, "r")
    print("\n")
    for linha in file:
        cont=0
        dados=linha.split("|")
        print("")
        for x in range(len(args)):
            print("%s: %s" % (args[cont], dados[cont]))
            cont+=1
    file.close()
