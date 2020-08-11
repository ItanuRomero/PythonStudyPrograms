'''Exercício Python 092: Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-o (com idade) em um dicionário. Se por acaso a CTPS for diferente de ZERO, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.'''
from datetime import datetime
dados_pessoa = {
    'nome': str(input('Nome: ')).strip().capitalize()
}
ano_nascimento = int(input('Ano de nascimento: '))
dados_pessoa['idade'] = datetime.today().year - ano_nascimento
carteira_de_trabalho = int(input('Numero da carteira de trabalho: (caso nao tenha, digite 0)'))
if carteira_de_trabalho != 0:
    dados_pessoa['CTPS'] = carteira_de_trabalho
    ano_contratacao = int(input('Ano de contratacao: '))
    dados_pessoa['aposentadoria'] = dados_pessoa['idade'] + ((ano_contratacao + 35) - datetime.today().year)
    dados_pessoa['salario'] = float(input('Salario: '))
else:
    dados_pessoa['CTPS'] = 'Nao possui'
print('-=' * 20)
for key, value in dados_pessoa.items():
    print(f'{key:-<10}{value:->10}.')
