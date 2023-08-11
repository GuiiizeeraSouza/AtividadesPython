#2 - Faça um programa que ajude motoristas calcular e estimar viagens com diferentes tempos de viagem.
#    O programa deve receber do usuário do sistema (motorista) a distância a ser percorrida e o tempo
#    desejado da viagem. A partir disso, o programa deve calcular e exibir na tela a velocidade média
#    necessária.

print("Olá Motorista!")

distancia_percorrida=int(input("Digite a distancia será percorrida(Em KM):"))
tempo_viajem=int(input("Digite o tempo deseja que dure a viajem(Em horas):"))

velocidade_media = distancia_percorrida/tempo_viajem

print(f'{velocidade_media:.0f}km/h')
