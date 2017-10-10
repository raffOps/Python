class quadrado:
    def __init__(self,lado):
        self.lado=lado
    def mudar(self):
        try:
            self.lado=float(input("Digite o novo tamanho do lado: "))
        except ValueError:
            quadrado.mudar()

    def retornar(self):
        print("Lado quadrado é %.2f" % self.lado)

    def area(self):
        print("Area do quadrado é %.2f" % (self.lado**2))

quadrado=quadrado(2)
quadrado.area()
quadrado.retornar()
quadrado.mudar()
quadrado.retornar()
quadrado.area()

