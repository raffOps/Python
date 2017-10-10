#Verifica se a entrada pode ser convertida para uma varável tipo int. Se sim, verifica se ele está num determinado periodo.
#  Se a e b estiverem com o valor 0, não há verificação de período
# A variável texto printa o texto definido no programa main
def validateDATA(texto,a,b,c):

    if a=="-" and b=="-":
        try:
            if c == "int":
                x = int(input("%s" % texto))
            elif c == "float":
                x = float(input("%s" % texto))
            return x
        except ValueError:
            return validateDATA(texto, a, b, c)


    elif a!="-" and b=="-":
        try:
            if c == "int":
                x = int(input("%s" % texto))
                if x < a:
                    while x < a:
                        x = int(input("%s" % texto))
            elif c == "float":
                x = float(input("%s" % texto))
                if x < a:
                    while x < a:
                        x = float(input("%s" % texto))
            return x
        except ValueError:
            return validateDATA(texto, a, b, c)


    elif a=="-" and b!="-":
        try:
            if c == "int":
                x = int(input("%s" % texto))
                if x > b:
                    while x > b:
                        x = int(input("%s" % texto))
            elif c == "float":
                x = float(input("%s" % texto))
                if x > b:
                    while x > b:
                        x = float(input("%s" % texto))
            return x
        except ValueError:
            return validateDATA(texto, a, b, c)


    elif a!="-" and b!="-":
        try:
            if c == "int":
                x = int(input("%s" % texto))
                if x > a or x < b:
                    while x > a or x < b:
                        x = int(input("%s" % texto))
            elif c == "float":
                x = float(input("%s" % texto))
                if x > a or x < b:
                    while x > a or x < b:
                        x = float(input("%s" % texto))
            return x
        except ValueError:
            return validateDATA(texto, a, b, c)