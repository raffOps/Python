linha=list(range(4))
matriz=[]
contadorLinha=0

while contadorLinha < 4:
    contadorColuna = 0
    while int(contadorColuna<4):
        linha[contadorColuna] = input(
            f"Digite o termo da linha {contadorLinha} coluna {contadorColuna}: "
        )
        contadorColuna+=1
    matriz.append([linha[0],linha[1],linha[2],linha[3]])
    contadorLinha+=1

contadorColuna=0
contadorLinha=0

print("\n\n")
while contadorLinha < 4:
    print(
        f"  {matriz[contadorLinha][0]}  {matriz[contadorLinha][1]}  {matriz[contadorLinha][2]}  {matriz[contadorLinha][3]}"
    )
    contadorLinha+=1

contadorLinha=0

print("\n")

while contadorLinha < 4:
    maior=matriz[contadorLinha][0]
    while int(contadorColuna)<4:
        if int(matriz[contadorLinha][contadorColuna])>int(maior):
            maior=matriz[contadorLinha][contadorColuna]
        contadorColuna+=1
    contadorColuna = 0

    print(f"Maior elemento da linha {contadorLinha} eh: {maior}")
    contadorLinha+=1

