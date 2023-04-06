#acrescentar elementos numa fila ou excluir o primeiro elemento
fila=list(range(10))
opcao=1
contador=0
tamanho=10

while (contador < 10):
    print("%d" % fila[contador])
    contador+=1
contador = 0

print("\n")
while True:
    opcao=int(input("\nDigite:\n1 para incluir uma elemento na fila\n2 para excluir o primeiro elemento da fila\n3 para sair\n\nSua opcao: "))
    print(opcao)
    if opcao == 1:
        elemento=input("\nDigite o elemento que você quer incluir na fila: ")
        fila.append(elemento)
        print("\nElemento %s incluido no final da fila" % (fila[-1]))
        tamanho += 1
        while (contador < tamanho):
            print("\n%s" % fila[contador])
            contador+=1
        contador = 0
    elif opcao == 2:
        tamanho-=1
        print("\nPrimeito elemento (%s) saiu da fila" % fila[0])
        fila.pop(0)
        while (contador < tamanho):
            print(f"{fila[contador]}")
            contador+=1
        contador = 0
    elif opcao == 3:
        break
