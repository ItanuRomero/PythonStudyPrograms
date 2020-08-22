# lista 02
# achei mais organizado desta forma, prof :)
# Itanu Romero - 2o. semestre.


def questao_01():
    """
    Faça um programa para calcular e exibir o desconto de INSS
    conforme o valor do salário digitado pelo usuário
    (incluindo centavos – cuidado com o uso do tipo de dados correto).
    """
    valor = float(input('Valor salario minimo: '))
    if valor <= 600.00:
        valor = valor - (valor * 0.07)
    elif 600.00 < valor <= 800.00:
        valor = valor - (valor * 0.09)
    elif 800.00 < valor <= 1200.00:
        valor = valor - (valor * 0.09)
    else:
        valor = valor - (valor * 0.11)
    print(f'Valor liquido a receber: {valor}')


def questao_02():
    """
    Faça um programa para calcular e exibir a porcentagem de comissão de
    vendas de um vendedor, conforme o volume
    mensal de vendas do mesmo digitado pelo usuário
    (incluindo centavos – cuidado com o uso do tipo de dados correto).
    """
    valor = float(input('Valor de vendas: '))
    if valor <= 5000.00:
        valor = valor * 0.02
    elif 5000.00 < valor <= 10000.00:
        valor = valor * 0.05
    elif 10000.00 < valor <= 15000.00:
        valor = valor * 0.07
    else:
        valor = valor * 0.09

    print(f'Valor da comissao: {valor}')


def questao_03():
    """
    Faça um programa para calcular e exibir a valor do imposto de ICMS de um
    produto, conforme a classificação do tipo de produto e do
    valor de custo do mesmo digitado pelo usuário
    (incluindo centavos – cuidado com o uso do tipo de dados correto).
    """
    valor = float(input('Valor do produto: R$'))
    tipo = input('Tipo de produto: ')
    if tipo == 'Cesta Básica':
        valor = 0
    elif tipo == 'Eletrônicos':
        valor = valor * 0.25
    elif tipo == 'Serviços':
        valor = valor * 0.18
    else:
        valor = valor * 0.12

    print(f'Valor do imposto: {valor}')


def questao_04():
    """
    Faça um programa para calcular e exibir o desconto de IR
    conforme o valor dosalário digitado pelo usuário
    (incluindo centavos – cuidado com o uso do tipo de dados correto).
    """

    valor = float(input('Insira o salario: '))
    if valor <= 1250.00:
        valor = 0
    elif 1250.00 < valor <= 1900.00:
        valor = valor * 0.11
    elif 1900.00 < valor <= 2700.00:
        valor = valor * 0.25
    else:
        valor = valor * 0.275

    print(f'Valor do desconto do IR: {valor}')


def questao_05():
    """
    Faça um programa para calcular e exibir a valor do imposto de
    ISS de uma nota fiscal de serviços, conforme o valor
    total de serviços especificado na mesma digitado pelo usuário
    (incluindo centavos – cuidado com o uso do tipo de dados correto).
    """

    valor = float(input('Digite o valor total de serviços: '))
    if valor <= 5000.00:
        valor = valor * 0.04
    elif 5000.00 < valor <= 10000.00:
        valor = valor * 0.06
    elif 1000.00 < valor <= 20000.00:
        valor = valor * 0.13
    else:
        valor = valor * 0.16

    print(f'Valor do imposto de ISS: {valor}')


def questao_06():
    """
    Faça um programa para calcular e exibir o desconto na compra do cliente,
    conforme o valor da compra do mesmo digitado pelo usuário
    (incluindo centavos – cuidado com o uso do tipo de dados correto).
    """
    valor = float(input('Valor de compra: '))
    if valor <= 50.00:
        valor = valor * 0.05
    elif 50.00 < valor <= 100.00:
        valor = valor * 0.08
    elif 100.00 < valor <= 150.00:
        valor = valor * 0.12
    else:
        valor = valor * 0.15

    print(f'Valor do desconto é: {valor}.')


def questao_07():
    """
    Faça um programa para calcular e exibir a valor dos juros de um
    empréstimo bancário, conforme o valor emprestado e o
    número de parcelas digitado pelo usuário
    (incluindo centavos – cuidado com o uso do tipo de dados correto).
    """

    valor = float(input('Digite o valor do empréstimo: '))
    parcela = int(input('Digite a quantidade de parcelas: '))
    if parcela <= 3:
        valor = valor * 0.06
    elif 3 < parcela <= 6:
        valor = valor * 0.09
    elif 6 < parcela <= 12:
        valor = valor * 0.22
    else:
        valor = valor * 0.34

    print(f'Valor do juros é {valor}')


def questao_08():
    """
    Faça um programa para calcular e exibir a quantidade de parcelas sem
    juros e o valor de cada parcela, conforme o valor da compra digitado pelo usuário
    (incluindo centavos – cuidado com o uso do tipo de dados correto).
    """

    valor = float(input('Digite o valor da compra: '))
    if valor <= 100.00:
        valor = valor / 2
        parcela = 2
    elif 100.00 < valor <= 200.00:
        valor = valor / 3
        parcela = 3
    elif 200.00 < valor <= 400.00:
        valor = valor / 4
        parcela = 4
    else:
        valor = valor / 5
        parcela = 5
    print(f'Sera em {parcela} parcelas de {valor}')


def questao_09():
    """
    Faça um programa para calcular e exibir o desconto na compra do cliente
    em uma farmácia, conforme o valor da compra do mesmo digitado pelo usuário
    (incluindo centavos – cuidado com o uso do tipo de dados correto).
    """
    valor = float(input('Digite o valor total de serviços: '))
    if valor <= 150.00:
        valor = valor * 0.05
    elif 150.00 < valor <= 300.00:
        valor = valor * 0.07
    elif 300.00 < valor <= 500.00:
        valor = valor * 0.10
    else:
        valor = valor * 0.20
    print(f'Valor do desconto é {valor}')


def questao_10():
    """
    Faça um programa para calcular e exibir a categoria do nadador, dado a sua idade.
    """
    idade = int(input('Digite a sua idade: '))
    if 5 <= idade < 8:
        categoria = 'Infantil A'
    elif 8 <= idade <= 10:
        categoria = 'Infantil B'
    elif 11 <= idade <= 13:
        categoria = 'Juvenil A'
    elif 14 <= idade < 17:
        categoria = 'Juvenil B'
    else:
        categoria = 'Senior'
    print(f'A categoria é {categoria}')


def questao_11():
    """
    Faça um programa que leia um número inteiro
    e diga se este é positivo, negativo ou zero.
    """
    valor = int(input('Digite um número: '))
    if valor < 0:
        status = 'Negativo'
    elif valor == 0:
        status = 'Zero'
    else:
        status = 'Positivo'
    print(f'Esse número é {status}.')


def questao_12():
    """
    Faça um programa que determine se um dado número é par ou ímpar.
    """
    numero = int(input('Digite um numero: '))
    if numero % 2 == 0:
        status = 'par'
    else:
        status = 'impar'
    print(f'O numero digitado é {status}')


def questao_13():
    """
    Faça um programa que simule uma calculadora com as quatro operações básicas
    (+, -, *, / ). O programa deve solicitar ao usuário a entrada de dois operandos
    e da operação a ser executada, na forma de menu. Dependendo da opção escolhida,
    deve ser executada a operação solicitada e escrito seu resultado.
    Utilize uma variável do tipo inteiro para armazenar a operação e utilize o
    comando caso para escolher a operação a ser executada a partir do operador.
    """
    valor1 = int(input('Digite um número: '))
    valor2 = int(input('Digite outro número: '))
    operacao = input('Escreva a operação: ').strip()
    if operacao == 'Multiplicação':
        valor = valor1 * valor2
    elif operacao == 'Soma':
        valor = valor1 + valor2
    elif operacao == 'Subtração':
        valor = valor1 - valor2
    elif operacao == 'Divisão':
        valor = valor1 / valor2
    else:
        valor = 'Operação não reconhecida'
    print(f'Resultado é: {valor}')


def questao_14():
    """
    Faça um programa que leia as repostas de três questões de múltipla escolha
    (a, b, c, d). Em seguida, leia o gabarito dessas questões,
    ou seja, as respostas corretas. Depois, compare as
    respostas dadas com as do gabarito e indique quantas respostas estão corretas
    """
    valor1 = str(input('7 vezes 8 é:\n'
                       ' a - 56\n'
                       ' b - 58\n'
                       ' c - 46\n'
                       ' d - 48\n')).lower()
    valor2 = str(input('\nRaíz quadrada de 81 é:\n'
                       ' a - 27\n'
                       ' b - 21\n'
                       ' c - 26\n'
                       ' d - 22\n')).lower()
    valor3 = input("\nMelhor cidade\n"
                   " a - Bragança Paulista\n"
                   " b - Sao Paulo\n"
                   " c - Atibaia\n"
                   " d - Jundiai\n")
    resultado = 0
    if valor1 == 'a':
        resultado = resultado + 1
    if valor2 == 'b':
        resultado = resultado + 1
    if valor3 == 'c':
        resultado = resultado + 1
    print(f'Vc acertou {resultado} questoes!')


def questao_15():
    """
    Faça um programa que leia três valores que representam os lados de um triângulo.
    Primeiramente, verifique se os lados podem formar um triângulo
    ( a soma de dois lados não pode ser menor que o terceiro lado ).
    Caso possa formar um triângulo, indique se este é
    equilátero, isósceles ou escaleno.
    """
    valor1 = int(input('Digite um lado: '))
    valor2 = int(input('Digite outro lado: '))
    valor3 = int(input('Digite outro lado: '))
    if (valor1 + valor2) < valor3 or (valor1 + valor3) < valor2 or (valor2 + valor3) < valor1:
        resultado = 'Não pode formar um triângulo!'
    elif valor1 == valor2 and valor1 == valor3:
        resultado = 'Triângulo Equilátero'
    elif (valor1 == valor2 and valor1 != valor3) or (valor2 == valor3 and valor1 != valor3) or (
            valor1 == valor3 and valor2 != valor3):
        resultado = 'Triângulo Isósceles'
    else:
        resultado = 'Triângulo Escaleno'
    print(f'Resultado é: {resultado}')


def questao_16():
    """
    Dado um ano d.C. (depois de Cristo), identifique se este é um ano bissexto ou não.
    Considere que para o ano ser bissexto basta que seja divisível por 400.
    Caso contrário, este precisará ser divisível por 4 e não ser divisível por 100.
    """
    valor = int(input('Digite um ano: '))
    if valor % 400 == 0 or (valor % 4 == 0 and valor % 100 > 0):
        status = 'Bissexto'
    else:
        status = 'Não é bissexto'
    print(f'Esse ano é {status}.')


def questao_17():
    """
    Faça um programa que calcule o IMC de uma pessoa
    (IMC = massa em kg / altura em metros elevado ao quadrado)
    e informe a sua classificação segundo a tabela a seguir:
    """
    massa = float(input('Digite a sua massa: '))
    altura = float(input('Digite a sua altura: '))
    imc = massa / (altura * altura)
    if imc < 17.00:
        status = 'Muito abaixo do peso'
    elif 17.00 <= imc < 18.50:
        status = 'Abaixo do pesoo'
    elif 18.50 <= imc < 25.00:
        status = 'Peso normal'
    elif 25.00 <= imc < 30.00:
        status = 'Acima do peso'
    elif 30.00 <= imc < 35.00:
        status = 'Obesidade I'
    elif 35.00 <= imc < 40.00:
        status = 'Obesidade II'
    else:
        status = 'Obesidade III (mórbida)'
    print(f'O seu IMC é {status}.')


def questao_18():
    """
    Efetuar a leitura de dois valores numéricos inteiros
    representados pelas variáveis A e B
    e apresentar o resultado da diferença do maior valor pelo menor.
    """
    valor1 = int(input('Insira o 1o.: '))
    valor2 = int(input('Insira o 2o.: '))
    if valor1 > valor2:
        resultado = valor1 - valor2
    else:
        resultado = valor2 - valor2
    print(f'O resultado do maior menos o menor é: {resultado}')


def questao_19():
    """
    Efetuar a leitura de um valor numérico inteiro positivo ou negativo
    representado pela variável N e apresentar o valor lido como sendo positivo.
    Dica: se o valor lido for menor que zero, o mesmo deve ser multiplicado por -1.
    """
    numero = int(input('INsira um numero: '))
    if numero < 0:
        numero += -1
    print(f'Numero em forma absoluta: {numero}')


def questao_20():
    """
    Ler os valores de quatro notas escolares bimestrais de um aluno representadas
    pelas variáveis N1, N2, N3, N4. Calcular a média aritmética (variável MD1)
    desse aluno e apresentar a mensagem "APROVADO" se a média obtida for maior ou
    igual a 7. Caso contrário, o programa deve solicitar a quinta nota
    (nota de exame, representada pela variável NE) do aluno e calcular uma nova média
    aritmética (variável MD2) entre a nota de exame e a primeira média aritmética.
    Se o valor da nova média for maior ou igual a cinco, apresentar a mensagem
    "APROVADO EM EXAME". Caso contrário, apresentar a mensagem "REPROVADO".
    Informar também,após a apresentação das mensagens,
    o valor da média obtida pelo aluno.
    """
    notas = list()
    soma = media = 0
    for contador in range(1, 5):
        notas.append(float(input(f'Insira a nota de numero {contador}: ')))
        soma += notas[contador - 1]
    media = soma / 4
    if 10 > media >= 7:
        status = 'Aprovado!'
    else:
        nota_de_exame = float(input(f'Insira a nota do exame: '))
        soma += nota_de_exame
        media = soma / 5
        if media >= 5:
            status = 'Aprovado em Exame'
        else:
            status = 'Reprovado'
    print(f'A situação do aluno é: {status}\n'
          f'A média do aluno é: {media}')


def questao_21():
    """
    Ler um número inteiro qualquer e multiplicá-lo por 2.
    Apresentar o resultado da multiplicação somente se o resultado for maior que 30. 
    """
    numero = int(input('Insira um numero: '))
    numero *= 2
    if numero > 30:
        print(f'Resultado da multiplicacao por 2: {numero}')


# MainProgram
# Para acessar as questoes chame a funcao correta, ex:
# questao_01()
# tambem e possivel ver o enunciado em:
# help(questao_01)
