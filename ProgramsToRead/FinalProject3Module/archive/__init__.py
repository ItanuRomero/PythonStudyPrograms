import interface

def does_not_exists(name):
    try:
        file = open(name, 'rt')
        file.close()
    except FileNotFoundError:
        return True
    else:
        return False


def create_file(name):
    file = open(name, 'wt+')
    file.close()


def read_file(name):
    try:
        file = open(name, 'rt')
    except FileNotFoundError:
        print('Erro ao ler arquivo, tente novamente.')
    else:
        interface.create_line()
        interface.create_title('Cadastros: ')
        export_data = file.readlines()

        print(interface.insert_cores('azul claro'), 'Nome', '\t'* 5,'Idade')
        for line in export_data:
            print(interface.insert_cores('azul'), line.replace(';', '\t\t\t\t\t'))
        print(interface.insert_cores('reset'))
        file.close()
        try:
            input('Pressione ENTER para continuar...')
        except:
            print('Redirecionando...')


def write_file(name):
    try:
        file = open(name, 'at')
    except FileNotFoundError:
        print('Erro, tente novamente...')
    else:
        interface.create_line()
        interface.create_title('CADASTRAR')
        file.write(input('Digite o nome: ').capitalize())
        file.write(';')
        file.write(input('Digite a idade: '))
        file.write('\n')
        file.close()
        interface.create_title('Cadastro feito!')
        input('Pressione ENTER para continuar...')
