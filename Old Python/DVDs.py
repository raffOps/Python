from MDvalidateDATA import validateDATA
from MDprintDATABASE import printDATABASE
from MDverifyCODE import verifyCODE
from MDeraseDATA import eraseDATABASE


ARQUIVO="DVDS"

def acrescentar(arquivo):
    file=open(arquivo,"a")
    codigo = verifyCODE(ARQUIVO)
    titulo = input("Titulo: ")
    diretor = input("Diretor: ")
    lançamento = str(validateDATA("Data de lançamento (entre 1950 e 2016): ", 2016, 1950, "int"))
    preço = str(validateDATA("Preço (entre R$ 10 e R$ 60 ): ", 60, 10, "float"))
    file.writelines([codigo,"|",titulo, "|", diretor, "|", lançamento, "|", preço,"|","\n"])
    file.close()

x=True
while x==True:
    opcao=validateDATA("\n1-Listar || 2 -Adicionar || 3-Excluir || 4-Sair\nDigite sua opcao: ",4,1,"int")
    if opcao==1:
        printDATABASE(ARQUIVO,"Código","Titulo", "Diretor", "Data de lançamento", "Preço")
    elif opcao==2:
        acrescentar(ARQUIVO)
    elif opcao==3:
        eraseDATABASE(ARQUIVO)
    elif opcao==4:
        x=False



