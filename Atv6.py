#6 - Construa um programa em Python em que o usuário insira a sigla de um estado brasileiro em que 
#    uma pessoa nasceu e, em seguida imprima uma das seguintes mensagens: 
#    Carioca Paulista Mineiro Outros estados


def main():
    estado = input("Digite a sigla do estado de nascimento (ex: SP): ").upper()

    if estado == "AC":
        print("Outros estados")
    elif estado == "AL":
        print("Outros estados")
    elif estado == "AP":
        print("Outros estados")
    elif estado == "AM":
        print("Outros estados")
    elif estado == "BA":
        print("Baiano")
    elif estado == "CE":
        print("Outros estados")
    elif estado == "DF":
        print("Outros estados")
    elif estado == "ES":
        print("Outros estados")
    elif estado == "GO":
        print("Outros estados")
    elif estado == "MA":
        print("Outros estados")
    elif estado == "MT":
        print("Outros estados")
    elif estado == "MS":
        print("Outros estados")
    elif estado == "MG":
        print("Mineiro")
    elif estado == "PA":
        print("Outros estados")
    elif estado == "PB":
        print("Outros estados")
    elif estado == "PR":
        print("Outros estados")
    elif estado == "PE":
        print("Outros estados")
    elif estado == "PI":
        print("Outros estados")
    elif estado == "RJ":
        print("Carioca")
    elif estado == "RN":
        print("Outros estados")
    elif estado == "RS":
        print("Gaúcho")
    elif estado == "RO":
        print("Outros estados")
    elif estado == "RR":
        print("Outros estados")
    elif estado == "SC":
        print("Outros estados")
    elif estado == "SP":
        print("Paulista")
    elif estado == "SE":
        print("Outros estados")
    elif estado == "TO":
        print("Outros estados")
    else:
        print("Sigla de estado inválida")

if __name__ == "__main__":
    main()
