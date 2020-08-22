# Ola professora, resolvi deixar dessa forma para que seja mais organizado!
# Itanu Romero.

def questao_1():
    """
    Questão 1. Faça um programa que receba três notas,
    calcule e mostre a média aritmética entre elas.
    Exiba, as notas, e a respectiva média.
    """
    num1, num2, num3 = float(input('Entre com a 1a. nota: ')), \
                       float(input('Entre com a 2a. nota: ')), \
                       float(input('Entre com a 3a. nota: '))
    media = (num1 + num2 + num3) / 3
    print(f'A média aritmética das notas é: {media}')


def questao_2():
    """
    Questão 2. Faça um programa que receba três notas e seus respectivos pesos,
    calcule e mostre a média ponderada dessas notas.
    Exiba, as notas, seus respectivos pesos e a média.
    """
    nota = list()
    peso = list()
    soma = media_ponderada = soma_pesos = 0
    for contador in range(0, 3):
        nota.append(float(input('Insira a primeira nota: ')))
        peso.append(int(input('Insira o peso da primeira nota: ')))
    for contador2 in range(0, 3):
        soma += nota[contador2] * peso[contador2]
        soma_pesos += peso[contador2]
    media_ponderada = soma / soma_pesos
    print(f'A média ponderada dessas notas é: {media_ponderada}')


def questao_3():
    """
    Questão 3. Faça um programa que receba o salário de um
    funcionário e o percentual de aumento,
    calcule e mostre o valor do aumento e o novo salário.
    """
    salario = float(input('Digite seu salário: R$'))
    porcentagem = float(input('Digite seu aumento em %: '))
    aumento = salario * (porcentagem / 100)
    salario_final = salario + aumento
    print(f'\nO seu novo salário é de R${salario_final}.\n'
          f'Houve um aumento de: R${aumento}')


def questao_4():
    """
    Questão 4. Faça um programa que receba o salário-base de um funcionário,
    calcule e mostre o salário a receber,
    sabendo-se que esse funcionário tem gratificação de 5% sobre o salário-base e
    paga imposto de 7% sobre salário-base.
    """
    salario_base = float(input('Digite seu salário: R$'))
    gratificacao = salario_base * 0.05
    imposto = salario_base * 0.07
    salario = salario_base + gratificacao
    salario = salario - imposto
    print(f'Seu salario final: R${salario}\n'
          f'recebeu uma gratificação de: R${gratificacao}.\n'
          f'Pagou um imposto de: R${imposto}.')


def questao_5():
    """
    Questão 5. Faça um programa que receba um número positivo e maior que zero,
    calcule e mostre:
    O número digitado ao quadrado;
    O número digitado ao cubo;
    A raiz quadrada do número digitado;
    A raiz cúbica do número digitado;
    A soma do quadrado mais o cubo do número digitado.
    """
    import math
    while True:
        try:
            numero = int(input('Insira um numero positivo: '))
        except:
            print('Ocorreu um ERRO inesperado, tente novamente: ')
        else:
            if numero > 0:
                break
            print('Favor inserir um número positivo e maior que 0.')
    quadrado = math.sqrt(numero)
    cubo = numero ** (1 / 3)
    print(f'O número ao quadrado: {numero ** 2}.\n'
          f'A número ao cubo é: {numero ** 3}.\n'
          f'A raíz quadrada do número é: {quadrado}.\n'
          f'A raíz cúbica do número é: {cubo}.\n'
          f'A soma do quadrado mais o cubo do número digitado é: {quadrado + cubo}.\n')


def questao_6():
    """
    Elaborar um programa que receba uma medida em pés
    e apresente o valor convertido em metros.
    """
    medida_em_pes = float(input('Insira a medida em pés: '))
    metros = medida_em_pes * 0.3048
    print(f'A medida é equivalente à {metros:.2f}m.\n')


def questao_7():
    """
    Elaborar um programa que calcule e apresente em metros por segundo
    o valor da velocidade de um projétil que percorre uma distância
    em quilômetros a um espaço de tempo em minutos.
    """
    km = float(input('Insira a distância em Km: '))
    minutos = float(input('Insira o tempo em minutos: '))
    hora = minutos / 60
    velocidade_kmh = km / hora
    velocidade = velocidade_kmh / 3.6
    print(f'A velocidade do projétil é de {velocidade:.2f}m/s.')


def questao_8():
    """
    Faça um programa que receba o número de horas trabalhadas e o valor do
    salário mínimo. Calcule e mostre o salário a
    receber seguindo as regras abaixo:
    - a hora trabalhada vale a metade do salário mínimo;
    - o salário bruto equivale ao número de horas trabalhadas multiplicado
    pelo valor da hora trabalhada;
    - o imposto equivale a 3% do salário bruto;
    - o salário a receber equivale ao salário bruto menos o imposto.
    """
    horas_trabalhadas = float(input('Digite suas horas trabalhadas: '))
    salario_minimo = float(input('Digite so valor do salario minimo: R$'))
    salario_bruto = horas_trabalhadas * (salario_minimo / 2)
    imposto = salario_bruto * 0.03
    salario_a_receber = salario_bruto - imposto
    print(f'O salario a receber é de: R${salario_a_receber}')


def questao_9():
    """
    Um trabalhador recebeu seu salário e o depositou em sua conta corrente bancária.
    Esse trabalhador emitiu dois cheques e agora deseja saber seu saldo atual.
    Sabe-se que cada operação bancária de retirada paga CPMF de 0,38%
    e o saldo inicial da conta está zerado.
    """
    salario = float(input('Valor do salario: R$'))
    cheque1, cheque2 = float(input('Valor do 1o. cheque: ')), \
                       float(input('Valor do 2o. cheque: '))
    cpmf1 = cheque1 * 0.0038
    cpmf2 = cheque2 * 0.0038
    conta = salario - (cheque2 + cheque1 + cpmf1 + cpmf2)
    print(f'O saldo atual em sua conta é: R${conta}')


def questao_10():
    """
    Pedro comprou um saco de ração com peso em quilos.
    Pedro possui dois gatos para os quais fornece a quantidade de ração em gramas.
    Faça um programa que receba o peso do saco de ração
    e a quantidade de ração fornecida para cada gato.
    Calcule e mostre quanto restará de ração no saco após cinco dias.
    """
    peso_saco_emkg = float(input('Peso do saco de ração em Kg: '))
    quantidade_racao = float(input('Quantidade para cada gato em gramas: '))
    # pois sao dois gatos
    quantidade_racao *= 2
    # transformando em gramas
    peso_saco_emkg *= 1000
    restante = peso_saco_emkg - (quantidade_racao * 5)
    print(f'Restará um total de {restante}g de ração.')


def questao_11():
    """
    Antes de o racionamento de energia ser decretado,
    quase ninguém falava em quilowatts; mas, agora,
    todos incorporam essa palavra em seu vocabulário.
    Sabendo-se que 100 quilowatts de energia custa um sétimo do salário mínimo,
    fazer um programa que receba o valor do salário mínimo e a
    quantidade de quilowatts gasta por uma residência e calcule. Imprima:
    o valor em reais de cada quilowatt,
    o valor em reais a ser pago,
    o novo valor a ser pago por essa residência com um desconto de 10%.
    """
    salario_minimo = float(input('Digite o salario minimo: R$'))
    quilowatts = int(input('Digite a quantidade de quilowatts: '))
    valor_kw = (salario_minimo / 7) / 100
    valor_em_reais = quilowatts * valor_kw
    com_desconto = valor_em_reais - (valor_em_reais * 0.10)
    print(f'O valor de cada quilowatt: {valor_kw:.2f},\n'
          f'O valor em reais a ser pago: {valor_em_reais:.2f}'
          f'O novo valor: {com_desconto}.')


def questao_12():
    """
     Criar um programa que efetue o cálculo da hora aula líquida
     (descontado o percentual de imposto) de um professor.
     Os dados fornecidos serão: valor da hora aula,
     número de aulas dadas no mês e percentual de desconto do INSS.
    """
    salario = float(input("Digite o valor do salário mínimo\n"))
    aulas = float(input("Digite o número de aulas dadas no mês\n"))
    inss = float(input("Digite o percentual de desconto do INSS\n"))
    valorLiq = (salario * aulas) - ((salario * aulas) * (inss / 100))
    print("Valor líquido que irá receber é", round(valorLiq, 2))


def questao_13():
    """
    Dado um polígono convexo de n lados,
    podemos calcular o número de diagonais diferentes (nd) desse polígono pela fórmula:
    nd = n * (n - 3) / 2. Fazer um programa que leia quantos lados tem o polígono,
    calcule e escreva o número de diagonais diferentes (nd) do mesmo.
    """
    lados = int(input("Digite a quantidade de lados\n"))
    diagonais = lados * (lados - 3)
    print(f'Quantidade de número de diagonais diferentes é: {diagonais}')


def questao_14():
    """
    Sabendo que a relação entre vértices, arestas e faces de um objeto geométrico
    é dada pela fórmula: vértices + faces = arestas + 2. Elabore um programa que
    calcule o número de vértices de um objeto geométrico genérico. A entrada será o
    número de faces e arestas (dadas por um número inteiro e positivo) e a
    saída será o número de vértices.
    """
    face = int(input("Digite a quantidade de faces\n"))
    aresta = int(input("Digite a quantidade de arestas\n"))
    if face > 0 and aresta > 0:
        vertices = aresta - face + 2
        print(f'Número de vértices: {vertices}')
    else:
        print('Apenas números inteiros e positivos')


def questao_15():
    """
    Elabore um programa que permita a entrada de dois valores ( x, y ),
    troque seus valores entre si e então exiba os novos resultados.
    """
    x = int(input('Valor de x: '))
    y = int(input('Valor de y: '))
    aux = x
    x = y
    y = aux
    print(f'Agora o valor de x: {x} e o de y: {y}')


def questao_16():
    """
    Elabore um programa que calcule e exiba a
    média aritmética de 5 números ( k, x, y, z, w).
    """

    k = float(input("Digite o valor de K\n"))
    x = float(input("Digite o valor de X\n"))
    y = float(input("Digite o valor de Y\n"))
    z = float(input("Digite o valor de Z\n"))
    w = float(input("Digite o valor de W\n"))
    media = (k + x + y + z + w) / 5
    print(f'O valor da media: {media}')


def questao_17():
    """
    Elabore um programa que calcule e exiba quantas notas de 50,
    10 e 1 são necessárias para se pagar uma conta cujo valor é fornecido
    """
    valor = int(input("Digite o valor à ser pago\n"))
    if valor >= 50:
        quant50 = valor // 50
        valor = valor - (quant50 * 50)
        if valor >= 10:
            quant10 = valor // 10
            valor = valor - (quant10 * 10)
            if valor < 10:
                quant1 = valor
    print(f'Sao necessarias:\n'
          f'{quant50} notas de 50.\n'
          f'{quant10} notas de 10\n'
          f'e {quant1} notas de 1.')


def questao_18():
    """
    Elabore um programa que calcule o alcance de um projétil, dada a velocidade (Vo),
    o ângulo (ang) entre o cano do canhão e o solo. A fórmula a ser utilizada é:
    S = (Vo Vo /g) sen(2ang), onde S é o alcance, g é a gravidade,
    ang é dado em graus, sendo necessário converter para radianos.
    """
    import math
    velocidade = int(input("Digite o valor da velocidade\n"))
    angulo = int(input("Digite o valor do ângulo em graus\n"))
    angRad = math.sin(2 * math.radians(angulo))
    alcance = (velocidade * velocidade / 9.81) * angRad
    print(f'O alcance e: {alcance:.2f}')


def questao_19():
    """
    Efetuar o cálculo e apresentar o valor de uma prestação de um bem em atraso,
    utilizando a fórmula:
    prestacao = valor + (valor (taxa / 100) tempo)
    """
    valor = float(input("Digite o valor da prestação\n"))
    taxa = float(input("Digite o valor da taxa\n"))
    tempo = int(input("Digite o valor da tempo (dia)\n"))
    prestacao = valor + (valor * (taxa / 100) * tempo)
    print(f'Valor de cada prestacao: {prestacao} se o tempo for {tempo}')


def questao_20():
    """
    Escreva um programa que calcule e exiba na tela o
    perímetro e área de uma circunferência.
    Dados: area = Pi raio ** 2, perimetro = 2 Pi * raio.
    """
    raio = float(input("Digite o valor do raio\n"))
    pi = 3.141592
    area = pi * (raio ** 2)
    perimetro = 2 * pi * raio
    print(f'Valor da area: {area}\n'
          f'perimetro: {perimetro}')


def questao_21():
    """
    Escreva um programa que solicite ao usuário dois números e
    apresente na tela os resultados das operações aritméticas
    (soma, subtração, multiplicação,
    divisão, resto da divisão, exponenciação, radiciação).
    """
    x = float(input('Valor de x: '))
    y = float(input('Valor de y: '))
    print(f'valor soma: {x + y}\n'
          f'Valor da subtração é: {x - y}\n'
          f'Valor da multiplicação é: {x * y}\n'
          f'Valor da divisão é: {x / y}\n'
          f'Valor do resto da divisão é: {x % y}\n'
          f'Valor da exponenciação é: {x ** y}\n'
          f'Valor da radiação é: {x ** (1 / y)}')


# MainProgram
# selecione a questao e tire o comentario:
# questao_"numero"()
# tambem e possivel ver qual o enunciado da questao com:
# help(questao_1)
# por exemplo...