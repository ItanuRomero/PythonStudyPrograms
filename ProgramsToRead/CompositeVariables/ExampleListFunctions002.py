'''Exercicio numero 82 do curso de python.
    Criar uma lista preenchida pelo usuario e utilizar esta para criar novas
    listas, no caso com numeros pares e impares.'''
lista_completa = list()
lista_pares = list()
lista_impares = list()
while True:
    lista_completa.append(int(input('Insira um valor: ')))
    resposta = str(input('Quer continuar? [s/n] ')).strip().lower()[0]
    while resposta not in 'sn':
        resposta = str(input('Erro. Apenas opcoes [s/n] ')).strip().lower()[0]
    if resposta in 'n':
        break
for valor in lista_completa:
    if valor % 2 == 0:
        lista_pares.append(valor)
    else:
        lista_impares.append(valor)
print('-=' * 30)
print(f'A lista completa: {lista_completa}')
print(f'Os numeros pares formam: {lista_pares}\n'
      f'Os numeros impares formam: {lista_impares}')
'''Criado por Itanu Romero.'''
