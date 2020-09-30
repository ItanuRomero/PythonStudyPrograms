"""Questão 2.A ACME Inc., uma empresa de 500 funcionários, está tendo problemas de espaço em disco no 
seu servidor de arquivos. Para tentar resolver este problema, o Administrador de Rede precisa saber 
qual o espaço ocupado pelos usuários, e identificar os usuários com maior espaço ocupado. Através de 
um programa, baixado da Internet, ele conseguiu gerar o seguinte arquivo, chamado "usuarios.txt":
alexandre 456123789
anderson 1245698456
antonio 123456456
carlos 91257581
cesar 987458
rosemary 789456125

Neste arquivo, o nome do usuário possui 15 caracteres. A partir deste arquivo, você deve criar um programa 
que gere um relatório, chamado "relatório.txt", no seguinte formato:

O arquivo de entrada deve ser lido uma única vez, e os dados armazenados em memória, caso sejam necessários, 
de forma a agilizar a execução do programa. A conversão da espaço ocupado em disco, de bytes para megabytes 
deverá ser feita através de uma função separada, que será chamada pelo programa principal. O cálculo do 
percentual de uso também deverá ser feito através de uma função, que será chamada pelo programa principal."""

def converter(num):
    num = num/1024
    num = num/1024
    return num
def percentualCalcula(lista, num):   
    num = float(num) * 100
    num = num / sum(lista)
    return num

arqEntrada = open("./usuarios.txt", "r")
lista = arqEntrada.readlines()
arqEntrada.close()
relatorio = "ACME Inc.  Uso do espaco em disco pelos usuarios\n"
relatorio += "--------------------------------------------------\n"
relatorio += "Nr.\tUsuario\t\tEspaco utilizado\t % do uso\n"
usuario = []
espaco = []
percentual = []
soma = 0

for numero in lista:
    soma += (float(numero[14:]))
for i in lista:
    usuario.append(i[0:14])
    num = converter(int(i[14:]))
    espaco.append(num)

for i in range (len(usuario)):
    percentualNum = percentualCalcula(espaco, espaco[i])
    percentual.append(percentualNum)
    relatorio += str(i+1) + "\t"
    relatorio += usuario[i] + "\t"
    relatorio += str(round((espaco[i]), 2)) + "\tMB" + "\t\t"
    relatorio += str(round((percentual[i]), 2)) + "\n"

arqSaida = open("./relatorio.txt", "w")
arqSaida.writelines(relatorio)

arqSaida.close()