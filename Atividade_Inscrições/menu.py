import os

from util import inscricao, conexao_base, conexao_base2, conexao_base3, listagem, entrada, saida

lista_inscritos = []
lista_entrada = []
lista_saida = []

conexao_base(lista_inscritos)
conexao_base2(lista_entrada)
conexao_base3(lista_saida)

while(True):
    os.system('cls')
    print("MENU")
    print('1- Inscrição')
    print('2- Listar inscritos')
    print('3- Registrar entrada')
    print('4- Registrar saida')
    print('5- Finalizar')
    op = input('Opções: ')

    if op == '1':
        print('Inscrição')

        inscricao(lista_inscritos)
    elif op == '2':
        print('Listagem de Inscritos')

        listagem()
    elif op == '3':
        print('Entrar')

        entrada(lista_inscritos)
    elif op == '4':
        print('Saída')

        saida(lista_inscritos)
    elif op == '5':
        print('Obrigado por usar o sistema')
        break
    else:
        print("opção inválidada")

    os.system('pause')
