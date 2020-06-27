total_compra = mais_barato = maiores_mil = 0
nome_mais_barato = ''
while True:
    nome_produto = str(input('Nome do produto: '))
    preco = float(input('preco: R$'))
    total_compra += preco
    if preco > 1000:
        maiores_mil += 1
    if preco < mais_barato or mais_barato == 0:
        mais_barato = preco
        nome_mais_barato = nome_produto
    resposta = ' '
    while resposta not in 'SN':
        resposta = str(input("Quer continuar? [s/n] ")).upper().strip()[0]
    if resposta == 'N':
        break
print(f'\n===PROGRAMA FINALIZADO===\n'
      f'Total gasto na compra: R${total_compra:.2f}\n'
      f'Foram registrados {maiores_mil} produtos maiores de mil reais\n'
      f'O nome do produto mais barato e: {nome_mais_barato}, '
      f'com o valor de R${mais_barato:.2f}')