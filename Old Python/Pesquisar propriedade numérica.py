# print xywz==(xy+wz)²

def separa(number):
    number1=number[:2]
    number2=number[2:]
    return [number1,number2]

print("Numeros que satisfazem a propriedade xywz==(xy+wz)²")
for CONT in range(1000, 10000):
    NUMBER=separa(str(CONT))
    x=(int(NUMBER[0]) + int(NUMBER[1]))**2
    if x==CONT:
        print(CONT)