cont=0
def fatorial(x):
    cont=1
    fatorial=1
    while(cont<=x):
        fatorial*=cont
        cont+=1
    return fatorial

def cosseno(numerador,denominador):
    cont=0
    soma=0
    while cont<30:
        numerador=numerador**denominador
        denominador=fatorial(denominador)
        print(denominador)
        if int(cont%2)==0:
            soma -= numerador / denominador
            print(soma)
        else:
            soma += numerador / denominador
        denominador+=2
        cont+=1
    return soma

print(1-cosseno(5,2))
