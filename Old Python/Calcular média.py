notas=list(range(5))
contador=0
soma=0

while(contador<len(notas)):
    notas[contador]=float(input("Digite a nota do aluno %d: " % contador))
    soma+=notas[contador]
    contador+=1

contador=0

while(contador<len(notas)):
    print("Nota do aluno %d: %.2f" % (contador, (notas[contador])))
    contador+=1

print("Media do alunos eh %f: " % (soma/5))




