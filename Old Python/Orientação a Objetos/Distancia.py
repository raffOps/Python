from MDvalidateDATA import validateDATA
class ponto:
    def __init__(self,x=0,y=0):
        self.x=x
        self.y=y

class retangulo:
    def __init__(self):
        self.base=validateDATA("Digite a o valor da base(entre 1 1000): ",1000,1,"float")
        self.altura = validateDATA("Digite a o valor da altura(entre 1 1000): ", 1000, 1, "float")

    def centro(self,Ponto):
        Ponto.x=self.base/2
        Ponto.y=self.altura/2


x="1"
while x=="1":
    Retangulo=retangulo()
    Ponto=ponto()
    Retangulo.centro(Ponto)
    print(Ponto.x,Ponto.y)

    x=input("Digite 1 para continuar ou quaklquer outra tecla pra sair: ")
