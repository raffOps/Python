class cachorro:
    def __init__(self,nome,cor,idade,personalidade):
        self.nome=nome
        self.cor=cor
        self.idade=idade
        self.personalidade=personalidade
    def irritar(self):
        if self.personalidade=="Calma":
            self.personalidade="Brabo"
        elif self.personalidade=="Brabo":
            self.personalidade="Muito brabo"

toby=cachorro("toby","preto",10,"Calma")
print(toby.personalidade)
toby.irritar()
print(toby.personalidade)
