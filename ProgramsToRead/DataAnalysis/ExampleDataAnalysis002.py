from os import system
system('clear')
total_maiores_18 = total_homens = total_mulheres = 0
while True:
    sexo = resposta = ' '
    print('~' * 10,
          'CADASTRO',
          '~' * 10)
    idade = int(input('DIgite a idade: '))
    while sexo not in 'MF':
        sexo = str(input('Digite o sexo: [M/F] ')).strip().upper()[0]
    if idade >= 18:
        total_maiores_18 += 1
    if sexo == 'M':
        total_homens += 1
    if sexo == 'F' and idade < 20:
        total_mulheres += 1
    while resposta not in 'SN':
        resposta = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resposta == 'N':
        break
system('clear')
print(f'==FIM PROGRAMA==\n'
      f'Foram cadastradas: \n{total_maiores_18} pessoas maiores de idade\n'
      f'{total_homens} Homens\n'
      f'{total_mulheres} Mulheres abaixo de 20 anos\n'
      f'Obrigado por utilizar este programa!')