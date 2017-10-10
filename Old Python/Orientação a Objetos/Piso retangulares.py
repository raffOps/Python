class retangulo:
    def __init__(self):
        self.base=float(input("Digite o tamanho da base dos azulejos: "))
        self.altura=float(input("Digite o tananho da altura dos azulejos: "))
    #def mudar_valores(self):
     #   self.base = float(input("Digite o tamanho da base: "))
      #  self.altura = float(input("Digite o tananho da altura: "))
    def area(self):
        area=float((self.base*self.altura))
        #print("\nA area eh %.2f" % area)
        return area
    def perimetro(self):
        perimetro=float(((2*self.base)+(2*self.altura)))
        #print("\nO perimetro é %.2f" % perimetro)
        return perimetro

azulejo=retangulo()
altura=float(input("Digite o tamanho da altura do piso: "))
base=float(input("Digite o tamanho da altura do piso: "))
quantidade=(altura*base)/azulejo.area()
print("Vão ser necessários %.2f azulejos para construir esso piso" % quantidade)