
#tudo errado
contadorLinha=0
contadorColuna=0
contadorPrint=0
elemento=list(range(4))

while contadorColuna<4:
    elemento[contadorColuna] = input("Digite o termo da linha %s e coluna %s: " % (contadorLinha, contadorColuna))
    contadorColuna += 1
matriz = (elemento[0], elemento[1], elemento[2], elemento[3])
contadorLinha+=1

while contadorLinha<4:
    contadorColuna = 0
    while contadorColuna<4:
        elemento[contadorColuna]=input("Digite o termo da linha %s e coluna %s: " % (contadorLinha,contadorColuna))
        contadorColuna+=1
    contadorLinha+=1
    matriz=matriz,(elemento[0],elemento[1],elemento[2],elemento[3])

print(matriz)
for x,y in matriz:
    print("\n %s  %s  %s  %s " % (x[0],x[1],x[2],x[3]))

