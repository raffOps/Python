#Verifica se a entrada pode ser convertida para uma varável tipo int. Se sim, verifica se ele está num determinado periodo.
#  Se a e b estiverem com o valor 0, não há verificação de período
# A variável texto printa o texto definido no programa main
def validateDATA(texto,a,b,c):

    if a=="-" and b=="-":
        try:
            if c == "int":
                x = int(input(f"{texto}"))
            elif c == "float":
                x = float(input(f"{texto}"))
            return x
        except ValueError:
            return validateDATA(texto, a, b, c)


    elif a!="-" and b=="-":
        try:
            if c == "int":
                x = int(input(f"{texto}"))
                if x < a:
                    while x < a:
                        x = int(input(f"{texto}"))
            elif c == "float":
                x = float(input(f"{texto}"))
                if x < a:
                    while x < a:
                        x = float(input(f"{texto}"))
            return x
        except ValueError:
            return validateDATA(texto, a, b, c)


    elif a == "-":
        try:
            if c == "int":
                x = int(input(f"{texto}"))
                if x > b:
                    while x > b:
                        x = int(input(f"{texto}"))
            elif c == "float":
                x = float(input(f"{texto}"))
                if x > b:
                    while x > b:
                        x = float(input(f"{texto}"))
            return x
        except ValueError:
            return validateDATA(texto, a, b, c)


    else:
        try:
            if c == "int":
                x = int(input(f"{texto}"))
                if x > a or x < b:
                    while x > a or x < b:
                        x = int(input(f"{texto}"))
            elif c == "float":
                x = float(input(f"{texto}"))
                if x > a or x < b:
                    while x > a or x < b:
                        x = float(input(f"{texto}"))
            return x
        except ValueError:
            return validateDATA(texto, a, b, c)