# Atividade 1)

#seleção

#repetição

#string

#lista

#Construir um Menu com operações: Menu 1 - Cadastrar funcionário 2 - Listar funcionários 3 - Excluir funcionários Opção:

#No programa, o usuário irá digitar, obrigatoriamente, um nome completo. O programa, a partir desse nome, vai gerar seu email com @ufn.edu.br. Por exemplo, Alexandre Zamberlan -> alexandre.zamberlan@ufn.edu.br. Próximo passo, este email deve ser inserido em uma lista que deve controlar duplicados. Na opção 3, o usuário deve digitar o email a ser excluído.

#Atividade 2) Gerar uma matriz NxN, onde o N é informado pelo Usuário. Essa matriz deve ter seus número embaralhados a partir do 0 até N*N.

import os

lista = []

while(True):
    os.system("cls")
    print("1 - Cadastrar funcionário")
    print("2 - Listar funcionários")
    print("3 - Excluir funcionários Opção")
    print("4 - Sair")
    opcao = input("Opção: ")    
    if (opcao == "1"):
        print("Cadastro de usuario: ")        
        while(True):
            nome_completo = input("Digite seu nome completo: \n")
            vetor_nomes = nome_completo.split(" ")
            if (len(vetor_nomes) <= 1):
                print("Seu nome deve ser digita completo!\n")
            else:
                break  
        
        email = vetor_nomes[0]+"."+ vetor_nomes[-1] + "@ufn.edu.br"
        email = email.lower()
        if lista.__contains__(email):
            print("Usuário com email já cadastrado")
        else:
            lista.append(email)
        lista.sort()        
    elif (opcao == "2"):
        print("Lista de funcionarios: \n")
        
        if (len(lista) == 0):
            print("Lista vazia!")
        else:
            for i in lista:
                print(i)        
    elif (opcao == "3"):
        print("Excluir funcionario: ")
        email = input("Digite o email para ser removido: \n")
        
        if lista.__contains__(email):
            lista.remove(email)
            print("Email Removido.")
            
        else:
            print("Email não enontrado!")
        
    elif (opcao == "4"):
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida!")
    
    os.system('pause')
