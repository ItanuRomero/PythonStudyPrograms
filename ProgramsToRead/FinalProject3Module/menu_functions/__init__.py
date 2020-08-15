from interface import *


def create_menu():
    create_line()
    create_title(f' MENU PRINCIPAL ')
    create_line()
    menu_options()
    create_line()
    opcao_usuario = input_option()
    process_option_user(opcao_usuario)


def menu_options():
    print(f'{insert_cores("amarelo")}1 - '
          f'{insert_cores("amarelo claro")}Ver pessoas cadastradas.\n'
          f'{insert_cores("amarelo")}2 - '
          f'{insert_cores("amarelo claro")}Cadastrar nova pessoa.\n'
          f'{insert_cores("amarelo")}3 - '
          f'{insert_cores("amarelo claro")}Sair do sistema. {insert_cores("reset")}')


def input_option():
    while True:
        try:
            opcao = int(input('Insira sua opcao: '))
        except ValueError:
            print('ERRO. Tente novamente apenas com numeros inteiros.')
        except KeyboardInterrupt:
            print('Usuario preferiu nao informar.')
        except Exception as erro:
            print(f'Tivemos um problema, segue:\n{erro}')
        else:
            if 0 < opcao < 4:
                return opcao
            else:
                print('Digite um valor valido.')


def process_option_user(opcao):
    print(opcao)