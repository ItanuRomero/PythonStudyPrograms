listagem = list()
for inserir in range(0, 5):
    listagem.append(int(input(f'insira um numero para a posicao {inserir}: ')))
menor = min(listagem)
maior = max(listagem)
print(f'O menor valor e: {menor}.\nO maior valor e: {maior}.')
print(f'o numero {menor} foi encontrado nas posicoes: ', end='')
for posicao, valor in enumerate(listagem):
    if valor == menor:
        print(f'{posicao}...', end='')
print(f'\ne o numero {maior} foi encontrado nas posicoes: ', end='')
for posicao, valor in enumerate(listagem):
    if valor == maior:
        print(f'{posicao}...', end='')
print()
