# Questão 3. Elabore um programa que utilize uma função que solicite 
# três argumentos, e que forneça a soma desses três argumentos.

def soma(x, y, z):
    print(f'A soma e: {x + y + z}')
x = int(input('Digite um número: '))
y = int(input('Digite um número: '))
z = int(input('Digite um número: '))
soma(x, y, z)
