# O nome das variáveis a,b e c devem ser definidos no programa main
def printDATABASE(arquivo, *args):
    with open(arquivo, "r") as file:
        print("\n")
        for linha in file:
            dados=linha.split("|")
            print("")
            for cont, _ in enumerate(range(len(args))):
                print(f"{args[cont]}: {dados[cont]}")
