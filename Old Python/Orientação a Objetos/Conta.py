##0 OBJETIVO ERA FAZER POR ORIENTAÇÃO A OBJETO, MAS TÁ FICANDO SEM QUERER NA FORMA ESTRUTURADA
from MDvalidateDATA import validateDATA
from MDverifyCODE import verifyCODE
from MDeditDATABASE import editDATABASE

class cliente:
    def __init__(self):
        self.nome=input("Digite o nome do cliente: ")
        self.conta=validateDATA("Digite o numero da conta (6 digitos): ",999999,100000,"int")
        self.senha=validateDATA("Digite a senha (6 digitos): ",999999,100000,"int")
        self.saldo=0

    def depositar(self):
        deposito=validateDATA("Digite a quantidade que quer depositar em sua conta(maximo R$ 1000 por operação): ",1000,0,"float")
        self.saldo+=deposito

    def sacar(self):
        print("Saldo disponivel para saque: %s" % self.saldo)
        saque=validateDATA("Digite a quantidade que quer sacar: ", self.saldo,0,"float")
        self.saldo-=saque

    def cadastrar(Cliente,arquivo):
        Cliente = Cliente.__dict__
        file=open(arquivo,"a")
        file.writelines([str(Cliente["conta"]), "|", str(Cliente["nome"]), "|", str(Cliente["senha"]), "|",str(Cliente["saldo"]),"|","\n"])


    def login(arquivo):
        login = editDATABASE(arquivo, "alterar", parametro)
        if login[1] == True:
            op = validateDATA("\nLogin realizado com sucesso\n1-Sacar|2-Depositar|3-Saldo|4-Sair\nDigite a sua opção: ",
                              4, 1, "int")
            if op == "1":


ARQUIVO="Banco"
x="1"
while(x=="1"):
    op=validateDATA("\nDigite a opção correspondente\n1-Cliente novo|2-Acessso a conta|3-Sair: ",3,1,"int")
    if op=="1":
        cliente.cadastrar(cliente(),ARQUIVO)
    if op=="2":
        login(ARQUIVO,"alterar")





