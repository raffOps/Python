def verifyCODE(arquivo):
    x=False
    codigo=input("Digite o código de entrada no banco de dados: ")
    with open(arquivo,"r") as file:
        for linha in file:
            dados = linha.split("|")
            if dados[0]==codigo:
                x=True
    if x==False:
        return codigo
    print("Código já existente nesse banco de dados")
    return verifyCODE(arquivo)