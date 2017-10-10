def menu(op1,op2,op3,op4):
    print("\n")
    x=input("1- %s: || 2- %s: || 3- %s: || 4- %s\nDigite sua opção: " % (op1,op2,op3,op4)))
    if x>"4" or x<"1":
        while x>"4" or x<"1":
            x = input("1- %s: || 2- %s: || 3- %s: || 4- %s\nDigite sua opção: " % (op1, op2, op3, op4)))
    return x


