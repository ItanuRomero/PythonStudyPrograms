# Questão 14. Elabore um programa que: Um quadrado mágico é aquele dividido 
# em linhas e colunas, com um número em cada posição e no qual a soma das linhas, 
# colunas e diagonais é a mesma. Por exemplo, veja um quadrado mágico de lado 3, 
# com números de 1 a 9:

import random
cubo = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]
satisfaz = True
def magicsquare():
    global satisfaz
    if cubo[0][0] + cubo[0][1] + cubo[0][2] == cubo[1][0] + cubo[1][1] + cubo[1][2] == cubo[2][0] + cubo[2][1] + cubo[2][2] == cubo[0][0] + cubo[1][0] + cubo[2][0] == cubo[0][1] + cubo[1][1] + cubo[2][1] == cubo[0][2] + cubo[1][2] + cubo[2][2] == cubo[0][0] + cubo[1][1] + cubo[2][2]:
        satisfaz = False

 
while satisfaz:
    vetor = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(3):
        for j in range(3):
            numero = random.choice(vetor)
            cubo[i][j] = numero
            vetor.remove(numero)
    magicsquare()
print(cubo[0][0], cubo[1][0], cubo[2][0])
print(cubo[0][1], cubo[1][1], cubo[2][1])
print(cubo[0][2], cubo[1][2], cubo[2][2])