alunos = dict()
notas = list()
while True:
    nome = str(input('Nome aluno: '))
    if nome == '':
        break
    nota1, nota2 = float(input('Nota 1: ')), float(input('Nota 2: '))
    notas.append(nota1)
    notas.append(nota2)
    alunos[nome] = notas[:]
    notas.clear()
while True:
    nome_aluno = str(input('Insira o nome do aluno: '))
    if nome_aluno in alunos:
        media = (alunos[nome_aluno][0] + alunos[nome_aluno][1]) / 2
        print(f'O aluno {nome_aluno} tem a media: {media}')
        break
    elif nome_aluno == '':
        break
    else:
        print('Nome n encontrado...')