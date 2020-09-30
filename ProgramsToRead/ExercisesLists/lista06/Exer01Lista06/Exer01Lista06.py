"""Questão 1. Faça um programa que leia um arquivo texto contendo uma lista de endereços IP e 
gere um outro arquivo, contendo um relatório dos endereços IP válidos e inválidos. O arquivo 
de entrada possui o seguinte formato:
200.135.80.9
192.168.1.1
8.35.67.74
257.32.4.5
85.345.1.2
1.2.3.4
9.8.234.5
192.168.0.256
E o arquivo de saída no seguinte formato:
[ Endereços válidos : ]
200.135.80.9
192.168.1.1
8.35.67.74
1.2.3.4
[ Endereços inválidos : ]
257.32.4.5
85.345.1.2
9.8.234.5
192.168.0.256"""

ipValido = list()
ipNaoValido = list()
arqEntrada = open("./entrada.txt", "r")

listaIp = arqEntrada.readlines()
arqEntrada.close()

for i in range (len(listaIp)):
    lista = listaIp[i].rsplit(".")
    if (len(lista) == 4 and int(lista[0]) <= 255 and int(lista[0]) >= 0 and int(lista[1]) <= 255 and int(lista[1]) >= 0 and int(lista[2]) <= 255 and int(lista[2]) >= 0 and int(lista[3]) <= 255 and int(lista[3]) >= 0):
        ipValido.append(listaIp[i])
    else:
        ipNaoValido.append(listaIp[i])

arqSaida = open("./saida.txt", "w")
arqSaida.write("[Enderecos validos:]\n")
arqSaida.writelines(ipValido)

arqSaida.write("[Enderecos invalidos:]\n")
arqSaida.writelines(ipNaoValido)

arqSaida.close()
