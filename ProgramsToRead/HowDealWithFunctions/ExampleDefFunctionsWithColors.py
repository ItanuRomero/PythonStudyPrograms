"""
Exercício Python 106: Faça um mini-sistema que utilize o Interactive Help do Python. O usuário vai digitar o comando e o manual vai aparecer. Quando o usuário digitar a palavra 'FIM', o programa se encerrará. Importante: use cores.
"""
def mensagem(texto, cor=''):
    print(cor, '-' * (len(texto) + 2))
    print(cor, ' ', texto)
    print(cor, '-' * (len(texto) + 2))
    print('\033[0;0m')


def inserir_comando():
    comando = str(input('Digite o comando: ')).strip()
    return comando


def mostrar_help(palavra):
    print(help(palavra))


def insert_cores():
    cores = {
        'preto': ['\033[1;30m', '\033[1;40m'],
        'vermelho': ['\033[1;31m', '\033[1;41m'],
        'verde': ['\033[1;32m', '\033[1;42m'],
        'amarelo': ['\033[1;33m', '\033[1;43m'],
        'azul': ['\033[1;34m', '\033[1;44m'],
        'magenta': ['\033[1;35m ', '\033[1;45m'],
        'cyan': ['\033[1;36m ', '\033[1;46m'],
        'cinza claro': ['\033[1;37m', '\033[1;47m'],
        'cinza escuro': ['\033[1;90m', '\033[1;100m'],
        'vermelho claro': ['\033[1;91m', '\033[1;101m'],
        'verde claro': ['\033[1;92m', '\033[1;102m'],
        'amarelo claro': ['\033[1;93m', '\033[1;103m'],
        'azul claro': ['\033[1;94m', '\033[1;104m'],
        'magenta claro': ['\033[1;95m', '\033[1;105m'],
        'cyan claro': ['\033[1;96m', '\033[1;106m'],
        'branco': ['\033[1;97m', '\033[1;107m'],
        'negrito': '\033[;1m',
        'inverte': '\033[;7m',
        'reset': '\033[0;0m'
    }
    return cores


# Main Program
colorir = insert_cores()
mensagem("BEM-VINDO AO INTERACTIVE HELP PROGRAM", colorir['vermelho'][1])
mensagem("TIRE SUAS DUVIDAS ABAIXO!", colorir['verde'][1])
while True:
    mensagem("Lembrando:\n"
             "Digite FIM para sair do programa.\n"
             "Digite q para sair do interactive help", colorir['vermelho'][0])
    duvida = inserir_comando()
    if duvida.upper() == 'FIM':
        break
    mostrar_help(duvida)
print('Obrigado por utilizar o programa!')
