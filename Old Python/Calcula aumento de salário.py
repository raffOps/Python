#Calcule o aumento de um salario

salario=float(input("Digite o salario: "))
porcent=float(input("Digite a porcentagem de aumento: "))

print("O valor do novo salario eh R$ %.2f" % (salario+(salario*(porcent/100))