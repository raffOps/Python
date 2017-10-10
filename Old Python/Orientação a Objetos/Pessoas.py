from MDvalidateDATA import validateDATA
class humano:
    def __init__(self):
        self.nome=input("Digite o nome: ")
        self.idade=validateDATA("Digite a idade(int): ",100,0,"int")
        self.peso=validateDATA("Digite o peso (float): ",200,0,"float")
        self.altura=validateDATA("Digite a altura (float): ",2.20,1,"float")

    def envelhecer(self):
        if self.idade<=21:
            self.idade+=1
            self.altura+=0.05
        else:
            self.idade+=1

    def engordar(self):
        engorda=validateDATA("Digite o quanto você engordou (float): ",100,0,"float")
        self.peso+=engorda

    def emagrecer(self):
        emagrecimento = validateDATA("Digite o quanto você emagrecer (float): ", 100, 0, "float")
        self.peso -= emagrecimento

    def crescer(self):
        crescimento= validateDATA("Digite o quanto você cresceu (float): ",2,0,"float")
        self.altura+=crescimento

João=humano()
print(João.altura)
João.envelhecer()
print(João.idade,João.altura)
João.envelhecer()
print(João.idade,João.altura)
João.envelhecer()
print(João.idade,João.altura)
João.engordar()
João.envelhecer()
print(João.idade,João.altura,João.peso)

