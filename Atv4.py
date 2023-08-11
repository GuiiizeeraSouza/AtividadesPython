#4 - O volume de um cubo é determinado através do produto da área da base pela altura, 
#    (mas as arestas do cubo possuem medidas iguais), então temos que:
#    V = Ab * a ou V = a * a * a → V = a³. A partir disso, faça um programa, adequando as variáveis
#    para receber medidas de uma piscina (altura, largura e comprimento), para responder o volume de
#    água necessário para enchê-la.

altura_piscina=int(input("Digite a altura da piscina:"))
largura_piscina=int(input("Digite a largura desta piscina:"))
comprimento_piscina=int(input("Digite o comprimento da piscina:"))

volume_piscina = comprimento_piscina*largura_piscina*altura_piscina

print(volume_piscina)