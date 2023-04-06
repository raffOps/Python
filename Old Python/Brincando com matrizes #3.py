
dados={}
codigo=0
continuar='s'
carrosTOP=0
empresa=[[0,0],[0,0],[0,0],[0,0]]
preferida=empresa[0][0]
melhor=empresa[0][1]
pospreferida=0
posmelhor=0

while continuar=='s':
    fabricante=int((input("\n\n1- Ford || 2- Chevrolet || 3- Ferrari || 4- Fiat\nDigite o código da empressa fabricante do carro: ")))
    if fabricante>4 or fabricante<1:
        while fabricante>4 or fabricante<1:
            print("\nEntrada iválida")
            fabricante = int((input("1- Ford || 2- Chevrolet || 3- Ferrari || 4- Fiat\nDigite o código da empressa fabricante do carro: ")))

    ano=int(input("Digite o ano de fabricação do carro: "))
    if ano>1950 or ano<1900:
        while ano>1950 or ano<1900:
            ano=int(input("Ano invalido. Esse sistema só aceita carros com de fabricação entrre 1900 e 1950. Digite um ano válido: "))

    condicao=int(input("\n1 - Ruim || 2 - Regular || 3 - Bom || 4 - ótimo\nDigite a opcao que mais adequada para a condição do carro: "))
    if condicao>4 or condicao<1:
        while condicao>4 or condicao<1:
            print("\nEntrada invalida")
            condicao = int(input("\n 1 - Ruim || 2 - Regular || 3 - Bom || 4 - ótimo\nDigite a opcao que mais adequada para a condição do carro: "))

    dados[codigo] = [fabricante,ano,condicao]
    codigo+=1
    continuar=input("Digite s se deseja continuar: ")


print("\n\n")
for x, value in dados.items():
    print(
        f"Código: {x} || Fabricante: {value[0]} || Ano de fabricao: {dados[x][1]} || Estado: {dados[x][2]}"
    )
    if dados[x][0]== 1:
        empresa[0][0]+= 1
        empresa[0][1]+=dados[x][2]
    elif dados[x][0] == 2:
        empresa[1][0] += 1
        empresa[1][1] += dados[x][2]
    elif dados[x][0] == 3:
        empresa[2][0] += 1
        empresa[2][1] += dados[x][2]
    else:
        empresa[3][0] += 1
        empresa[3][1] += dados[x][2]

for x in range(4):
    if empresa[x][1]!=0:
        empresa[x][1]=empresa[x][1]/empresa[x][0]

print("\n\nCarros considerados muito bem conservados: ")
for x, value_ in dados.items():
    if (
        value_[1] < 1910
        and dados[x][2] == 3
        or (dados[x][1] < 1910 and dados[x][2] == 4)
    ):
        print(
            f"Código: {x} || Fabricante: {dados[x][0]} || Ano de fabricao: {dados[x][1]} || Estado: {dados[x][2]}"
        )
        carrosTOP+=1
if int(carrosTOP)==0:
    print(" ----- Nenhum carro antendeu ao requisitos para entrar nessa lista")

for cont, x in enumerate(range(4)):
    if empresa[x][0]>preferida:
        preferida=empresa[x][0]
        pospreferida=cont
    if empresa[x][1]>melhor:
        melhor=empresa[x][1]
        posmelhor=cont
if int(pospreferida)==0:
    print("Fabricante preferida: Ford")
elif int(pospreferida)==1:
    print("Fabricante preferida: Chevrolet")
elif int(pospreferida)==2:
    print("Fabricante preferida: Ferrari")
elif int(pospreferida)==3:
    print("Fabricante preferida: Fiat")

print("\n")

if int(posmelhor)==0:
    print("Fabricante com os melhores carros: Ford")
elif int(posmelhor)==1:
    print("Fabricante com os melhores carros: Chevrolet")
elif int(posmelhor)==2:
    print("Fabricante com os melhores carros: Ferrari")
else:
    print("Fabricante com os melhores carros: Fiat")