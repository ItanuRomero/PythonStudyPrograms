import menu_functions as menu
import archive

data = 'registrations.txt'
if archive.does_not_exists(data):
    archive.create_file(data)

while True:
    option_user = menu.create_menu()
    if option_user == 1:
        print(option_user)
        archive.read_file(data)
    elif option_user == 2:
        print(option_user)
        archive.write_file(data)
    else:
        print('Finalizando programa...\n'
              'Criado por Itanu Romero.')
        break
