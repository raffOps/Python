linha=list(range(4))
matriz=[]
contadorLinha=0

while int(contadorLinha)<4:
    contadorColuna = 0
    while int(contadorColuna<4):
        linha[contadorColuna]=input("Digite o termo da linha %s coluna %s: "% (contadorLinha,contadorColuna))
        contadorColuna+=1
    matriz.append([linha[0],linha[1],linha[2],linha[3]])
    contadorLinha+=1

contadorColuna=0
contadorLinha=0

print("\n\n")
while int(contadorLinha)<4:
    print("  %s  %s  %s  %s"% (matriz[contadorLinha][0],matriz[contadorLinha][1],matriz[contadorLinha][2],matriz[contadorLinha][3]))
    contadorLinha+=1

contadorLinha=0

print("\n")

while int(contadorLinha)<4:
    maior=matriz[contadorLinha][0]
    while int(contadorColuna)<4:
        if int(matriz[contadorLinha][contadorColuna])>int(maior):
            maior=matriz[contadorLinha][contadorColuna]
        contadorColuna+=1
    contadorColuna = 0

    print("Maior elemento da linha %s eh: %s" % (contadorLinha, maior))
    contadorLinha+=1

