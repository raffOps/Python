#Peca um numero do usuario ate o numero digitado atender as condicpes impostas pelo laco

numero=input("Digite um numero entre 0 e 10: ")
while numero<0 or numero>10:
    numero=input("Numero invalido. Digite um numero entre 0 e 10: ")
print("O numero digitado entre 0 e 10 foi %d" % numero)
