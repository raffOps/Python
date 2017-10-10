class _2d(object):
    def __init__(self,nome):
        self.nome=nome


class circulo(_2d):
    def __init__(self,nome,raio):
        super().__init__(nome)
        self.raio=raio

    def area(self):
        self.area=3.14*self.raio**2

class quadrado(_2d):
    def __init__(self,nome,lado):
        super().__init__(nome)
        self.lado=lado
    def area(self):
        self.area=self.lado**2


forma1=circulo('forma1',3)
forma1.area()
print(forma1.area)
print(forma1.nome)

forma2=quadrado("forma2",4)
forma2.area()
print(forma2.nome)
print(forma2.area)