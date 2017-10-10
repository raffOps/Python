# NUMEROS DE LINHAS E COLUNAS DEVE SER ESPECIFICADO NO PROGRAMA MAIN
def completeMATRIX(linhas,colunas):
    import random
    matrix=[]
    for x in range(linhas):
        lista=[]
        for y in range(colunas):
            lista.append(random.randint(1,30))
        matrix.append(lista)
    return matrix
