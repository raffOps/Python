def makeMATRIX(arquivo):
    with open(arquivo, "r") as file:
        data = []
        for linha in file:
            dados = linha.split("|")
            data.append(dados)
    return data


def makeFILE(arquivo,dado):
    for entrada in dado:
        for x in entrada:
            if x == entrada[-1]:
                file.writelines(x)
            else:
                file.writelines([x, "|"])
    file.close()
