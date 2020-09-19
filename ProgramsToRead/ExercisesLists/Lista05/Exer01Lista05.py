# Questão 1. Elabore um programa que imprima um número por linha até atingir o número 
# informado pelo usuário. Use uma função que receba um número inteiro informado pelo usuário e 
# imprima até a n-ésima linha.

def imprimir(numero):
    for x in range(1, numero + 1):
        numeroFor = x
        for y in range(x):
            print(numeroFor, end=" ")
        print("\n")
numero = int(input('Digite um número:'))
imprimir(numero)
