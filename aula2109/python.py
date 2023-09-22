import os


lista_inscritos = [
    
       
]

arquivo = open("inscricoes.txt", "a")


def MenuInscricao():
    print("MENU")
    print("1 - Fazer inscrição: ")
    print("2 - Listar Inscrições: ")
    print("3 - Entrar no evento: ")
    print("4 - Sair do evento: ")
    print("5 - Sair")

    opcao = input("Opção: ")


    if(opcao == "1"):
        print("Cadastro de usuario: ")        
        while(True):

                #Pegando o nome do usuario.
            nome_completo= input("Digite seu nome completo: \n")
            if lista_inscritos.__contains__(nome_completo):

                print("Usuário já cadastrada")
            else:
                 lista_inscritos.append(nome_completo)

                #Pega o email do usuario. 
            email = input("Digite seu Email: \n")
            if lista_inscritos.__contains__(email):

                print("Email já cadastrada \n" )
            else:
                 lista_inscritos.append(email)
                

                #Pegando matricula do usuario.
            matricula = input("Digite seu matricula completo: \n")

            if lista_inscritos.__contains__(matricula):

                print("Usuário com matricula já cadastrada \n")
            else:
                 lista_inscritos.append(matricula ) 
                    
            arquivo.writelines(lista_inscritos) #guarda a lista de matricula no arquivo usuario.
            break
MenuInscricao()