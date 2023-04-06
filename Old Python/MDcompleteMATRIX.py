# NUMEROS DE LINHAS E COLUNAS DEVE SER ESPECIFICADO NO PROGRAMA MAIN
def completeMATRIX(linhas,colunas):
    import random
    matrix=[]
    for _ in range(linhas):
        lista = [random.randint(1,30) for _ in range(colunas)]
        matrix.append(lista)
    return matrix
