def create_menu():
    create_line(40)
    print(f'{"MENU PRINCIPAL":-^40}')
    menu_options()
    create_line(40)
    opcao_usuario = input_option()
    process_option_user(opcao_usuario)


def menu_options():
    print('1 - Ver pessoas cadastradas.\n'
          '2 - Cadastrar nova pessoa.\n'
          '3 - Sair do sistema.')


def create_line(tamanho):
    print('-' * tamanho)


def input_option():
    while True:
        try:
            opcao = int(input('Insira sua opcao: '))
        except ValueError:
            print('ERRO. Tente novamente apenas com numeros inteiros.')
        except opcao > 2:
            print('ERRO. Favor entrar com apenas com as opcoes listadas')
        except Exception as erro:
            print(f'Tivemos um problema, segue:\n{erro}')
        else:
            return opcao


def process_option_user(opcao):
    print(opcao)