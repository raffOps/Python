from MDvalidateDATA import validateDATA
from MDverifyCODE import verifyCODE

def increaseDATABASE(arquivo):
    empresa=input("\nFord || Ferrari || Fiat || Chevrolet\nDigite o nome da empresa: ")
    if empresa!="Ford" and empresa!="Ferrari" and empresa!="Fiat" and empresa!="Chevrolet":
        while empresa!="Ford" and empresa!="Ferrari" and empresa!="Fiat" and empresa!="Chevrolet":
            empresa = input("Ford || Ferrari || Fiat || Chevrolet\nDigite o nome da empresa: ")

    ano=str(validateDATA("\nDigite a data de fabricação, que deve ser entre 1900 e 1950: ",1950,1900))
    estado=str(validateDATA("\n1- Ruim || 2- Regular || 3-Bom || 4-ótimo\nDigite a opção correspondente: ",4,1))
    print("\n")
    codigo=str(verifyCODE("arquivo"))
    if codigo==1:
        while codigo==1:
            codigo = str(code("arquivo"))


    file=open(arquivo,"a")
    file.writelines([empresa,"|",ano,"|",estado,"|",codigo,"|","\n"])
    file.close()

def decreaseDATABASE(arquivo):
        x=False
        codigo=input("Digite o código da entrada que você quer excluir: ")
        file = open(arquivo, "w+")
        for linha in file:
            dados = linha.split("|")
            if dados[3] == codigo:
                linha=len(dados[0])+len(dados[1])+len(dados[2])+len(dados[3])+5
                for x in range(linha):
                    file.write("\b")
                x=True
        if x==True:
            print("Entrada excluída do banco de dados")
        elif x==False:
            print("Essa entrada não está no banco de dados")

while True:

    OP=validateDATA("\n1-Listar || 2-Adicionar || 3-Excluir || 4-Sair\nDigite sua opção: ",4,1)
    if OP==1:
        print("\n")
        printDATABASE("arquivo","Empresa","Ano de Fabricação","Estado","Código")
    elif OP==2:
        increaseDATABASE("arquivo")
    ##elif OP==3:
      ##  decreaseDATABASE("arquivo")
    else:
        break