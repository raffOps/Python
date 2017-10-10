class Grupo(list):
    def __init__(self):
        self.pessoas=Pessoa()
    def __str__(self): #sobrecarga do método print. Irá printar os dados de todas as pessoas do grupo
        str=""
        for pessoa in self.pessoas: #percorre a lista e vai adicionando os dados das pessoas há uma string única
            str+="\nNome: %s || Idade: %d"%(pessoa.nome,pessoa.idade)
        return str #retorna a string

    def sort(self):
        copia = self.pessoas[:]
        tamanho = len(self.pessoas)
        self.pessoas[:] = []
        while len(self.pessoas) < tamanho:
            min = copia[0]
            for pessoa in copia:
                if pessoa.idade < min.idade:
                    min = pessoa
            copia.remove(min)
            self.pessoas.append(min)

class Pessoa():
    def __init__(self, nome=None, idade=None):
        self.nome = nome
        self.idade = idade


pedro = Pessoa("Pedro", 23)
ana = Pessoa("Ana", 13)
maria = Pessoa("Maria", 45)
rafa=Pessoa("Rafa",10)
grupo = Grupo()
grupo.pessoas = [pedro, ana, maria,rafa]
print(grupo)
grupo.sort()
print(grupo)

