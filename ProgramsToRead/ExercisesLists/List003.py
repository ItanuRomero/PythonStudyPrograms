# veja o fim da pagina para mais info.

def questao_01():
    """
    ma empresa decidiu fazer um levantamento em relação aos candidatos que se
    apresentarem para preenchi- mento de vagas em seu quadro de funcionários.
    Supondo que você seja o programador dessa empresa, faça um programa que leia,
    para cada candidato, a idade, o sexo (M ou F),e a experiência no serviço (S ou N).
    Para encerrar a entrada de dados, digite a idade igual a zero.
    O programa também deve calcular e mostrar:
        O número de candidatos do sexo feminino.
        O número de candidatos do sexo masculino.
        A idade média dos homens que já tem experiência no serviço.
        A porcentagem dos homens com mais de 45 anos entre o total dos homens.
        O número de mulheres com idade inferior a 21 anos e com experiência no serviço.
        A menor idade entre as mulheres que já tem experiência no serviço.
    """
    menor_idade_fem = 150
    quant_fem = 0
    quant_exp_fem = 0
    quant_masc = 0
    quant_exp_masc = 0
    quant_idade_masc = 0
    soma_idade_masc = 0
    while True:
        idade = int(input('Digite a sua idade: '))
        if idade == 0:
            break
        sexo = input("Digite o seu sexo (M ou F)\n")
        experiencia = input("Têm experiência no serviço (S ou N)\n")
        if sexo == "F":
            quant_fem = quant_fem + 1
            if experiencia == "S":
                if menor_idade_fem > idade:
                    menor_idade_fem = idade
                if idade <= 21:
                    quant_exp_fem = quant_exp_fem + 1
        if sexo == "M":
            quant_masc = quant_masc + 1
            if experiencia == "S":
                soma_idade_masc = soma_idade_masc + idade
                quant_exp_masc = quant_exp_masc + 1
            if (idade >= 45):
                quant_idade_masc = quant_idade_masc + 1
    if quant_fem == 0:
        menor_idade_fem = 0
    print(f'O número de candidatos do sexo feminino: {quant_fem}')
    print(f'O número de candidatos do sexo masculino: {quant_masc}')
    print(f'A idade média dos homens que já tem experiência no serviço: {soma_idade_masc / quant_exp_masc}')
    print(f'A porcentagem dos homens com mais de 45 anos entre o total dos homens: {quant_idade_masc}')
    print(f'O número de mulheres com idade inferior a 21 anos e com experiência no serviço: {quant_exp_fem}')
    print(f'A menor idade entre as mulheres que já tem experiência no serviço: {menor_idade_fem}')


def questao_02():
    """
    Faça um programa que receba o valor do salário mínimo,
    e a quantidade de quilowatts gasta por um consumidor e o tipo de consumidor
    (1-residencial, 2-comercial, 3-industrial) e que calcule e mostre:
        O valor de cada quilowatt, sabendo que o quilowatt custa um
        oitavo do salário mínimo.
        O valor a ser pago por consumidor (conta final mais o acréscimo).
        O faturamento geral da empresa,
        A quantidade de consumidores que pagam entre 500,00 e 1000,00.
        Terminar a entrada de dados ao digitar uma
        quantidade de quilowatt igual a zero.
        O acréscimo encontra-se na tabela a seguir:
    """
    faturamento = 0
    valorWatt = 0
    valorTotal = 0
    quantCons = 0
    while True:
        salario = float(input('Digite o salário mínimo: '))
        watts = float(input('Digite a quantidade de quilowatts gasto: '))
        if watts == 0:
            break
        consumidor = int(input('Seu tipo de consumidor (1-residencial, 2-comercial, 3-industrial)\n'))
        valorWatt = salario / 8
        valorWatts = watts * valorWatt
        if consumidor == 1:
            valorTotal = valorWatts + (valorWatts * 0.05)
        elif consumidor == 2:
            valorTotal = valorWatts + (valorWatts * 0.1)
        elif consumidor == 3:
            valorTotal = valorWatts + (valorWatts * 0.15)
        faturamento = faturamento + valorTotal
        if 500 <= valorTotal <= 1000:
            quantCons = quantCons + 1
        print(f'Valor de cada QuiloWatt: {valorWatt}')
        print(f'Valor pago do consumidor: {valorTotal}')
    print(f'Faturamento Total da empresa: {faturamento}')
    print(f'Quantidade de consumidores que pagam entre R$ 500,00 e R$ 1000,00: {quantCons}')


def questao_03():
    """
    Faça um programa que receba o número sorteado por um dado em vinte jogadas.
    Exibir os números sorteados e a frequência com que cada um aparece.
    """
    sorteioUm = 0
    sorteioDois = 0
    sorteioTres = 0
    sorteioQuatro = 0
    sorteioCinco = 0
    sorteioSeis = 0
    for item in range(20):
        dado = int(input('Digite o número sorteado: '))
        print(f'Número sorteado foi {dado}')
        if dado == 1:
            sorteioUm = sorteioUm + 1
        elif dado == 2:
            sorteioDois = sorteioDois + 1
        elif dado == 3:
            sorteioTres = sorteioTres + 1
        elif dado == 4:
            sorteioQuatro = sorteioQuatro + 1
        elif dado == 5:
            sorteioCinco = sorteioCinco + 1
        elif dado == 6:
            sorteioSeis = sorteioSeis + 1
    print(f'O número 1 foi sorteado {sorteioUm} vezes')
    print(f'O número 2 foi sorteado {sorteioDois} vezes')
    print(f'O número 3 foi sorteado {sorteioTres} vezes')
    print(f'O número 4 foi sorteado {sorteioQuatro} vezes')
    print(f'O número 5 foi sorteado {sorteioCinco} vezes')
    print(f'O número 6 foi sorteado {sorteioSeis} vezes')


def questao_04():
    """
    Uma empresa de ônibus com 48 poltronas (24 nas janelas e 24 no corredor).
    Faça um programa que controle o uso das poltronas ocupadas no corredor e na
    janela. Considere que 0 representa poltrona desocupada e 1, poltrona ocupada.
    Inicialmente, todas as poltronas estarão livres.
    Depois disso, o programa deverá exibir as seguintes opções:
    1 - Vender passagens
    2 - Mostrar mapa de ocupações do ônibus
    Quando a opção escolhida for Vender passagens, deverá ser perguntado
    se o usuário deseja janela ou corredor e o número da poltrona.
    O programa deverá dar uma das seguintes mensagens:
    Venda efetivada (se a poltrona solicitada estiver livre, marcando-a como ocupada).
    Poltrona ocupada (se a poltrona não estiver disponível para a venda).
    Ônibus lotado (quando todas as poltronas estiverem ocupadas).
    """
    corredor = list()
    janelas = list()
    for contador in range(1, 49):
        if contador % 2 == 0:
            corredor.append(contador)
        else:
            janelas.append(contador)
    while True:
        print(f'{" MENU ":-^40}')
        print(f'1 - Vender passagens.\n'
              f'2 - Mostrar poltronas ocupadas.\n'
              f'3 - Sair.\n')
        escolha = int(input('Digite a opção: '))
        if escolha == 3:
            break
        elif escolha == 1:
            while True:
                comprar = int(input('Insira o numero de uma poltrona: '))
                if comprar in janelas:
                    confirmar = str(input(f'Confirma a compra da poltrona'
                                          f' {comprar}? s/n')).strip().lower()[0]
                    if confirmar == 's':
                        janelas.remove(comprar)
                    break
                elif comprar in corredor:
                    confirmar = str(input(f'Confirma a compra da poltrona'
                                          f' {comprar}? s/n')).strip().lower()[0]
                    if confirmar == 's':
                        corredor.remove(comprar)
                    break
                else:
                    print('Não encontrado, tente novamente!')
            input('Pressione qualquer tecla para continuar!')
        elif escolha == 2:
            print(f'{" JANELA ":-^40}')
            for cadeira in janelas:
                print(cadeira, end=' - ')
                if cadeira % 10 == 1:
                    print()
            print()
            print(f'{" CORREDOR ":-^40}')
            for cadeira in corredor:
                print(cadeira, end=' - ')
                if cadeira % 10 == 0:
                    print()
            print()
            input('Pressione qualquer tecla para continuar!')
        else:
            print('Erro, tente novamente: ')







def questao_05():
    """
    Faça um programa que apresente os quadrados de
    números inteiros existentes na faixa de valores de 15 a 200.
    """
    for contador in range(15, 201):
        print(f'O quadrado de {contador} é: {contador ** 2}')


def questao_06():
    """
    Questão 6. Faça um programa que apresente a soma dos
    cem primeiros números naturais (1+2+3+4+5+...+98+99+100).
    """
    soma = 0
    for contador in range(1, 101):
        soma += contador
    print(f'A soma dos cem primeiros números naturais é: {soma}')


def questao_07():
    """
    Faça um programa que apresente os resultados da soma e da
    média aritmética dos valores pares situados na faixa numérica de 50 a 70.
    """
    soma = quantidade = 0
    for contador in range(50, 71):
        soma += contador
        quantidade += 1
    media = soma / quantidade
    print(f'A média é igual a {media}')


def questao_08():
    """
    Faça um programa que leia valores positivos inteiros
    até que um valor negativo seja informado.
    Ao final devem ser apresentados o maior e o menor valores informados pelo usuário.
    """
    maior = menor = contador = 0
    while True:
        valor = int(input('Insira um valor: '))
        if valor < 0:
            break
        if contador == 0:
            maior = valor
            menor = valor
        elif valor > maior:
            maior = valor
        elif valor < menor:
            menor = valor
        contador +=1
    print(f'\nMaior valor: {maior}\n'
          f'Menor vaor: {menor}\n'
          f'Numero de valores inseridos: {contador}.')


def questao_09():
    """
    Faça um programa que leia quinze valores numéricos inteiros
    e no final apresente o somatório e a média aritmética dos valores lidos.
    """
    soma = 0
    for contador in range(1, 16):
        numero = int(input(f'Insira o {contador}o. numero: '))
        soma += numero
    media = soma / 15
    print(f'Média aritmética dos valores lidos: {media}')


def questao_10():
    """
    Faça um programa que apresente todos os valores
    numéricos inteiros ímpares situados na faixa de 0 a 2000.
    """
    for contador in range(0, 2001):
        if contador % 2 == 1:
            print(contador, end=', ')
    print('FIM')


def questao_11():
    """
    Faça um algoritmo que apresente todos
    os valores numéricos divisíveis por 4 e menores que 200.
    """
    for contador in range(0, 201):
        if contador % 4 == 0:
            print(contador, end=', ')
    print('FIM')


# Teste cada um das questoes abaixo, ex:
# questao_04()
# ou veja o enunciado da questao:
# help(questao_04)
