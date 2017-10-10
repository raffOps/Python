#Informe o tipo de tringulo a partir do tamanho dos seus lados infromados pelo usuario

ladoA=float(input("Lado A: "))
ladoB=float(input("Lado B: "))
ladoC=float(input("Lado C: "))

if ladoA==ladoB and ladoA==ladoC:
    print("Triangulo equilatero")
elif ladoA==ladoB or ladoA==ladoC or ladoB==ladoC:
    print("Triangulo isosceles")
else:
    print("Triangulo escaleno")