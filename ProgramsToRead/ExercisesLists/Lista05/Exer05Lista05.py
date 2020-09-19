# Questão 5. Elabore um programa que utilize uma função chamada soma_imposto. 
# A função possui dois parâmetros formais: taxaImposto, que é a quantia de 
# imposto sobre vendas expressa em porcentagem e custo, que é o custo de um 
# item antes do imposto. A função “altera” o valor de custo para incluir o imposto 
# sobre vendas.

def soma_imposto(taxaImposto, custo):
    return custo + (taxaImposto / 100 * custo)
imposto = int(input('Quantia de imposto sobre vendas expressa em porcentagem: '))
custo = float(input('Custo do produto: '))
custo = soma_imposto(imposto, custo)
print(f'O custo com o imposto é {custo}')