class ponto:
    def __init__(self,a,b):
        self.x=a
        self.y=b

    def print(self):
        print("Ponto x: ",self.x,"Ponto y: ", self.y)

class retangulo:
    def __init__(self,base_,altura_):
        self.base=base_
        self.altura=altura_
        self.pontoCentro=ponto(0,0)
    def encontroCentro(self):
        self.pontoCentro.x=self.base/2
        self.pontoCentro.y=self.altura/2

    def print(self):
        print("Base: ",self.base," |  Altura: ",self.altura)
        self.pontoCentro.print()

retangulo1=retangulo(4,2)
retangulo1.encontroCentro()
retangulo1.print()

retangulo2=retangulo(12,13)
retangulo2.encontroCentro()
retangulo2.print()





