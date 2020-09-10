arquivo = open('dado.txt', 'r+')

nome = arquivo.readline().strip()
nota1 = arquivo.readline().strip()
nota2 = arquivo.readline().strip()
nota1 = int(nota1)
nota2 = int(nota2)
media = (nota1 + nota2) / 2
print(f'Nome do aluno: {nome}\n'
      f'Nota 1: {nota1}\n'
      f'Nota 2: {nota2}\n'
      f'Media: {media}')
arquivo.close()
