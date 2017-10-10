LISTA=[]
OP=1

def imprime():
    global LISTA
    print(LISTA)

def acrescenta():
    global LISTA
    x = input("Digite o novo elemento da lista: ")
    LISTA.append(x)

def decrescenta():
    global LISTA
    if len(LISTA) != 0:
        x=input("Digite qual elemento você quer excluir da lista: ")
        if x in LISTA:
            LISTA.remove(x)
        else:
            print("%s não está na lista" % x)
    else:
        print("Lista vazia")

def menu(OP):
    if int(OP)==1:
        imprime()
    elif int(OP)==2:
        acrescenta()
    elif int(OP)==3:
        decrescenta()

while True:
    OP=input("1-Listar ||  2-Acrescentar || 3-Descrescentar || 4-Sair\nDigite sua opcao: ")
    if OP>'4' or OP<'1':
        while OP>'4' or OP<'1':
            OP =input("Opção inválida\n1-Listar ||  2-Acrescentar || 3-Descrescentar || 4-Sair\nDigite sua opcao: ")
    if int(OP)==4:
        break
    menu(OP)
    print("\n")



