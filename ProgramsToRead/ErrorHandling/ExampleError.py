"""
Exercício Python 113: Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
"""

def leiaInt(mensagem):
    value = 0
    while True:
        try:
            value = int(input(mensagem))
        except KeyboardInterrupt:
            print('O usuario decidiu nao informar o numero')
            break
        except:
            print('Ocorreu um erro, certifique-se de que digitou um numero inteiro...')
        else:
            break
    return value


def leiaFloat(mensagem):
    value = 0
    while True:
        try:
            value = float(input(mensagem))
        except KeyboardInterrupt:
            print('\n\nO usuario decidiu nao informar o numero')
            break
        except:
            print('Ocorreu um erro, certifique-se de que digitou um numero inteiro...')
        else:
            break
    return value


# MainProgram
try:
    number1 = leiaInt('insira um numero inteiro: ')
    number2 = leiaFloat('insira um numero real:')
except:
    print('Erros localizados, da proxima insira os dados corretamente')
finally:
    print(f'o numero int {number1} e o real {number2}')
