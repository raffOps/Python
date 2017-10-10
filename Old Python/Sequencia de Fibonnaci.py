#imprime os numeros da sequencia de fibonnaci até determinado numero

termo1=1
termo2=1
soma=0
limite=int(input("Digite o numero delimitador da sequencia: "))

print("\n1\n1")
while(soma<=limite):
    soma=termo1+termo2
    if soma<=limite:
        print("%d  " % soma)
    termo1=termo2
    termo2=soma
