#3 - Refaça o programa anterior (refatorar) para que o programa recebe a distância e a velocidade média,
#    mas calcule e exiba o tempo da viagem.

print("Olá Motorista!")

distancia_percorrida=int(input("Digite a distancia será percorrida(Em KM):"))
velocidade_media=int(input("Digite a velocidade (Em Km/h):"))

tempo_viajem = distancia_percorrida/velocidade_media

print(f'{tempo_viajem:.0f} Horas')