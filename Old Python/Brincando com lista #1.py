#juntar duas listas

lista1=list(range(5))
lista2=list(range(5))
lista3=list(range(10))
contador=0

print("\n Lista 1")
while(contador<5):
    lista1[contador]=input("Digite um termo qualquer: ")
    contador+=1

contador=0

print("\n Lista 2")
while(contador<5):
    lista1[contador]=input("Digite um termo qualquer: ")
    contador+=1

lista3=lista3+lista1+lista2

contador=0

print("\n Lista 3")
while(contador<10):
    print(lista3[contador])
    contador+=1







