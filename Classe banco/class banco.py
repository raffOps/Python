class Banco(object):
    __total=1000
    reserva=__total*0.1
    def podefazeremprestimos(self,valor):
        return Banco.__total - valor > Banco.reserva

class Conta(Banco):
    def __init__(self,saldo=0,id=0,senha=0):
        self.__saldo=saldo
        self.__id=id
        self.__senha=senha
    def deposito(self,senha,valor):
        if senha == self.__senha:
            self.__saldo+=valor
        else:
            print("Senha incorreta")
    def saque(self,senha,valor):
        if senha == self.__senha:
            if self.__saldo>valor:
                self.__saldo-=valor
            else:
                print("Sem saldo suficiente")
        else:
            print("Senha incorreta")
    def podereceberemprestimos(self,valor):
        return bool(self.__saldo > valor and Conta.podefazeremprestimos(self,valor))
    def getsaldo(self,senha):
        return self.__saldo if senha==self.__senha else "Senha incorreta"


conta1=Conta(100,7845,"abcd")
print(conta1.getsaldo("akbcd"))
print(conta1.getsaldo("abcd"))
print(conta1.podereceberemprestimos(200))
conta1.deposito("abcd",80000)
print(conta1.podereceberemprestimos(200))
conta1.saque("abcd",1000000000)
