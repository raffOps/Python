# print xywz==(xy+wz)²

def separa(number):
    number1=number[:2]
    number2=number[2:]
    list=[number1,number2]
    return list

CONT=1000
print("Numeros que satisfazem a propriedade xywz==(xy+wz)²")
while int(CONT)<=9999:
    NUMBER=separa(str(CONT))
    x=(int(NUMBER[0]) + int(NUMBER[1]))**2
    if x==CONT:
        print(CONT)
    CONT+=1