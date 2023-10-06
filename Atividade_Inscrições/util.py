def conexao_base(lista):
    try:
        leitor = open('inscricoes.dat','r')
        for linha in leitor:
            vetor_linha = linha.split(';')
            lista.append(vetor_linha[0])
        leitor.close()
    except:
        pass

def conexao_base2(lista_entrada):
    try:
        leitor = open('inscricoes.dat','r')
        for linha in leitor:
            vetor_linha = linha.split(';')
            lista_entrada.append(vetor_linha[0])
        leitor.close()
    except:
        pass

def conexao_base3(lista_saida):
    try:
        leitor = open('entrada.dat','r')
        for linha in leitor:
            vetor_linha = linha.split(';')
            lista_saida.append(vetor_linha[0])
        leitor.close()
    except:
        pass

def inscricao(lista):
    matricula = input('Digite sua matricula: ')
    if matricula in lista:
        print('Esta matricula ja esta cadastrada no evento!')
    else:
        lista.append(matricula)
        nome = input('Nome: ')
        nome = nome.upper()
        email = input('Email: ')
        email = email.lower()
        escritor = open('inscritos.dat','a')
        escritor.write(matricula + ';' + nome + ';' + email + '\n')
        escritor.close()

def listagem():
    try: 
        leitor = open('inscritos.dat', 'r', encoding='utf8')
        for linha in leitor:
            vetor_linha = linha.split(';')
            print('Nome:',vetor_linha[1],'Matrícula:',vetor_linha[0])

        leitor.close()

    except:
        print('Sem inscrições até o momento')

def entrada(lista_entrada):
    matricula = input('Informa a sua matricula: ')
    if matricula in lista_entrada:
        lista_entrada.append(matricula)
        hora = input("Informe a hora de entrada: ")
        escritor = open('entrada.dat', 'a')
        escritor.write('Matricula: ' + matricula + '; ' + 'Hora de entrada: ' + hora + '\n')
        escritor.close()
        print("Entrada no evento confirmada!")
    else:
        print('Matricula não registrada')

def saida(lista_saida):
    matricula = input('Informe a sua matricula: ')
    if matricula in lista_saida:
        lista_saida.append(matricula)
        hora = input("Informe a hora de saida: ")
        escritor = open('saida.dat', 'a')
        escritor.write('Matricula: ' + matricula + '; ' + 'Hora de saida: ' + hora + '\n')
        escritor.close()
        print("Saida do evento confirmada!")
    else:
        print('Matricula não esta no evento')




