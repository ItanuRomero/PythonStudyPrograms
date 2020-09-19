# Questão 6. Elabore um programa que utilize uma função que converta da 
# notação de 24 horas para a notação de 12 horas. Por exemplo, o programa 
# deve converter 14:25 em 2:25 P.M. A entrada é dada em dois inteiros. 
# Deve haver pelo menos duas funções: uma para fazer a conversão e uma 
# para a saída. Registre a informação A.M./P.M. como um valor ‘A’ para 
# A.M. e ‘P’ para P.M. Assim, a função para efetuar as conversões terá 
# um parâmetro formal para registrar se é A.M. ou P.M. Inclua um loop que 
# permita que o usuário repita esse cálculo para novos valores de entrada 
# todas as vezes que deseja.

def converta(hora, minuto):
    if 0 < hora <= 12 and 0 < minuto < 60:
        saida(hora, minuto, 'A')
    elif 12 < hora < 24 and 0 < minuto < 60:
        saida(hora - 12, minuto, 'P')
    else:
        print('Não foi possível fazer a conversão')
def saida(hora, minuto, horario):
    if(horario == 'P'):
        print(hora,":",minuto,'PM')
    else:
        print(hora,":",minuto,'AM')

while True:
    hora = int(input('Hora: '))
    minuto = int(input('Minuto: '))
    converta(hora, minuto)
