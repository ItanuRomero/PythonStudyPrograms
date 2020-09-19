# Questão 13. Construa uma função que desenhe um retângulo usando os 
# caracteres ‘+’ , ‘−’ e ‘| ‘. Esta função deve receber dois parâmetros, 
# linhas e colunas, sendo que o valor por omissão é o valor mínimo 
# igual a 1 e o valor máximo é 20. Se valores fora da faixa forem informados, 
# eles devem ser modificados para valores dentro da faixa de forma elegante.

def retangulo(largura, altura):
    if largura > 20:
        largura = 20
    elif largura <= 0:
        largura = 1
    if altura > 20:
        altura = 20
    elif altura <= 0:
        altura = 1
    print('-+-' * largura)
    z = '|'
    for i in range(altura):
        print(z, ' ' * (largura * 3 - 4), z)
    print('-+-' * largura)
largura = int(input('Digite a largura: '))
altura = int(input('Digite a altura: '))
retangulo(largura, altura)