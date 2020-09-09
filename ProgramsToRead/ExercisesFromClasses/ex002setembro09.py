arquivo = open('dado.txt', 'w+')
while True:
    if arquivo.read() == '':
        print('Arquivo esta vazio')
        aluno = [str(input('Nome do aluno: ')), str(input('Nota 1: ')), str(input('Nota 2: '))
        ]
        for dados in aluno:
            arquivo.write(dados)
            arquivo.write('\n')
        arquivo.close()
    else:
        nome = arquivo.readline()
        nota1 = int(arquivo.readline())
        nota2 = int(arquivo.readline())
        media = (nota1 + nota2) / 2
        print(f'Nome do aluno: {nome}\n'
              f'Nota 1: {nota1}\n'
              f'Nota 2: {nota2}\n'
              f'Media: {media}')
        arquivo.close()
    resposta = str(input('Abrir novamente? [s/n]')).strip().lower()[0]
    if resposta == 'n':
        break