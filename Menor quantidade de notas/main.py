from MDvalidateDATA import validateDATA

quantia=validateDATA("Digite a quantia de dinheiro, sendo no máximo 1000 R$: ",1001,-1,"int")

notas_100=0
notas_50=0
notas_25=0
notas_10=0
notas_1=0

if quantia>=100:
    notas_100=quantia//100
    quantia-=notas_100*100

if quantia>=50:
    notas_50=quantia//50
    quantia-=notas_50*50

if quantia>=25:
    notas_25=quantia//25
    quantia-=notas_25*25

if quantia>=10:
    notas_10=quantia//10
    quantia-=notas_10*10

notas_1=quantia

print("Notas de 100 R$: ",notas_100,"\nNotas de 50 R$: ",notas_50,"\nNotas de 25 R$: ",notas_25)
print("Notas de 10 R$: ",notas_10,"\nNotas de 1 R$: ",notas_1)

