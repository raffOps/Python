from MDvalidateDATA import validateDATA
from MDeditFILE import makeMATRIX
from MDeditFILE import makeFILE

def editDATABASE(arquivo,modo):

    parametro = validateDATA("Digite o numero da conta no banco de dados que você quer excluir: ", 999999, 100000,
                             "int")
    data=makeMATRIX(arquivo)

    if modo=="excluir":
        flag = False
        for entrada in data:
            if entrada[0] == parametro:
                data.remove(entrada)
                flag = True
        if flag == False:
            print("Nenhum conta no banco de dados com esse código")
        elif:
            makeFILE(arquivo,*data)

    elif modo=="alterar":
        flag= False
        for entrada in data:
            if entrada[0] == parametro:
                senhadigitada=validateDATA("\nDigite a senha da conta %s: " % entrada[0],999999,100000,"int")
                if senhadigitada!=entrada[-2]:
                    while senhadigitada!=entrada[-2] or senhadigitada!="1":
                        senhadigitada = validateDATA("\nSenha incorreta\nDigite a senha da conta %s ou digite 1 para sair: " % entrada[0],"-", "-",
                                                     "int")
                        if senhadigitada=="1":
                            print("\nOperação cancelada")
                            return False
                        elif senhadigitada==entrada[-2]:
                            x=[data,True]
                            return x
                flag= True
        if flag == False:
            print("Nenhum conta no banco de dados com esse código")


    file = open(arquivo, "w")
    for entrada in data:
        for dado in entrada:
            if dado == entrada[-1]:
                file.writelines(dado)
            else:
                file.writelines([dado, "|"])
    file.close()
