def verifyCODE(arquivo):
    x=False
    codigo=input("Digite o código de entrada no banco de dados: ")
    file=open(arquivo,"r")
    for linha in file:
        dados = linha.split("|")
        if dados[0]==codigo:
            x=True
    file.close()
    if x==False:
        return codigo
    else:
        print("Código já existente nesse banco de dados")
        return verifyCODE(arquivo)