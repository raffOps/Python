lista=list(range(10))

for item in lista:
    lista[item]=input("\nDigite o numero %i para colocar na lista: " % item)

for item in lista:
    print(item)