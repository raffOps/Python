opcao='s'
notas={}
somamedia=0
cont=0
while opcao=='s':
    nome=input("Digite o nome do aluno: ")
    p1=float(input("Digite a nota da prova 1: "))
    p2=float(input("Digite a nota do prova 2: "))
    t1=float(input("Digite a nota do trabalho 1: "))
    media=(p1+p2+t1)/3
    somamedia+=media
    cont+=1
    notas.update({nome:[p1,p2,t1,media]})
    opcao=(input("Digite s se deseja continuar: "))

print("\n\nMedia da turma: %s" % (somamedia/cont))

for x in notas:
    print("\n\nNome: %s -- Nota P1: %s -- Nota P2: %s -- Nota T1: %s" % (x,notas[x][0],notas[x][1],notas[x][2]))
    if float(notas[x][3])>=6:
        print("Media: %s -- Aluno aprovado" % notas[x][3])
    elif float(notas[x][3])>=4:
        print("Media: %s -- Aluno em recuperacao" % notas[x][3])
    else:
        print("Media: %s -- Aluno reprovado" % notas[x][3])