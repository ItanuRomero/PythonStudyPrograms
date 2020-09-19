# Questão 9. Elabore um programa que utilize uma função que retorne 
# o reverso de um número inteiro informado. Por exemplo: 127 -> 721.

def inverter(numero):
    print(str(numero)[::-1])
num = int(input('Digite um número: '))
inverter(num)