# Lista 04 - Itanu Romero - 2o. semestre

def questao01():
    """
    Elabore um programa que efetue a leitura de duas strings e informe o seu conteúdo,
    seguido de seu compri- mento. Indique também se as
    duas strings possuem o mesmo comprimento e se são iguais ou diferentes no conteúdo.
    """
    dicionario = {}
    for i in range(2):
        palavra = input('Digite uma palavra: ')
        dicionario[i] = [palavra, len(palavra)]
    print(dicionario)
    if dicionario[0][0] == dicionario[1][0]:
        print('Conteúdo iguais')
    if dicionario[0][1] == dicionario[1][1]:
        print('Comprimento iguais')


def questao02():
    """
    Elabore um programa que solicite ao usuário, o seu nome e em seguida
    mostre o seu nome de trás para frente utilizando somente letras maiúsculas.
    """
    nome = input('Digite seu nome: ')
    print(nome[::-1].upper())


def questao03():
    """
     Elaborar um programa que solicite a digitação de um número
     de CPF no formato xxx.xxx.xxx-xx e indique se é um número válido ou inválido
     através da validação dos dígitos verificadores e dos caracteres de formatação.
    """
    cpf = input("Digite seu CPF\n")
    if len(cpf) == 14 and cpf[3] == "." and cpf[7] == "." and cpf[11] == "-":
        print("É um CPF")
    else:
        print("Não é um CPF")


def questao04():
    """
    Elaborar um programa que a partir da digitação de uma frase,
    o programa informe quantos espaços
    em branco e quantos são, e quantas vezes aparecem cada uma das vogais a, e, i, o, u.
    """
    frase = input('Digite uma frase: ').lower()
    vogais = ['a', 'e', 'i', 'o', 'u']
    vogais_na_frase = 0
    espacos_em_branco = 0
    for i in frase:
        if i in vogais:
            vogais_na_frase += 1
        if i in " ":
            espacos_em_branco += 1
    print(f'Numeros de vogais: {vogais_na_frase}')
    print(f'Numeros de espacos em branco: {espacos_em_branco}')


def questao05():
    """
    Faça um programa que leia um número de telefone,
    e corrija o número no caso deste conter somente 7 dígitos,
    acrescentando o ’3’ na frente.
    O usuário pode informar o número com ou sem o traço separador.
    """
    telefone = input('Digite um telefone: ')
    traco = False
    for i in telefone:
        if i == '-':
            traco = True
    if len(telefone) == 7 or len(telefone) == 8 and traco:
        telefone = '3' + telefone
    print(f'Seu telefone é: {telefone}')


def questao06():
    """
    Desenvolva um jogo em que o usuário tenha que adivinhar uma palavra que
    será mostrada com as letras embaralhadas. O programa terá uma lista de
    palavras lidas de uma lista a ser fixada inicialmente pelo programador e
    escolherá uma aleatoriamente. O jogador terá uma única tentativa para adivinhar
    a palavra. Ao final a palavra deve ser mostrada na tela, informando se o usuário
    ganhou ou perdeu o jogo.
    Observação: Refaça, possibilitando ao jogador tentar até 5 vezes.
    """
    import random
    animais = ['gato', 'cachorro', 'cavalo', 'jumento', 'peixe', 'zebra', 'papagaio', 'girafa', 'pomba', 'lagosta']
    escolhida = random.choice(animais)
    shuffled = list(escolhida)
    random.shuffle(shuffled)
    shuffled = "".join(shuffled)
    print(f'A palavra embaralhada é {shuffled}\n')
    tentativa = input('Qual a palavra embaralhada? ')
    if escolhida == tentativa.lower():
        print('Você acertou, parabéns')
    else:
        print('Você errou')
    print(f'A palavra era {escolhida}')


def questao07():
    """
     Elabore um programa que efetue a leitura de
     cinco números inteiros, adicione-os a uma lista e mostre-a.
    """
    lista = []
    for i in range(5):
        numero = int(input('Digite o um número: '))
        lista.append(numero)
    print(lista)


def questao08():
    """
    Elabore um programa que efetue a leitura de quinze números inteiros,
    adicione-os a uma lista e mostre-a de forma invertida, do último para o primeiro.
    """
    lista = []
    for i in range(15):
        numero = int(input('Digite o um número: '))
        lista.append(numero)
    print(lista[::-1])


def questao09():
    """
    Elabore um programa que efetue a leitura de quatro notas reais,
    adicione-as a uma lista e mostre-as, inclusive a média aritmética,
    arredondar duas casas decimais. Verifique e exiba as devidas mensagens
    se o aluno está aprovado ou não, considerando que a média de aprovação
    é maior ou igual a 7.0, e em prova exame, se
    média aritmética entre 4.0 e menor que 7.0. E reprovado, se menor que 4.0.
    """
    lista = []
    soma = 0
    for i in range(4):
        nota = float(input('Digite sua nota: '))
        soma = soma + nota
        lista.append(nota)
    media = round(soma / 4, 2)
    print(f'Suas notas são {lista}sendo assim sua média é {media}')
    if media >= 7:
        print('Você está aprovado')
    elif 4 <= media < 7:
        print('Pegou exame')
    else:
        print('Reprovou')


def questao10():
    """
    Faça um programa que leia uma lista com dez caracteres,
    e diga quantas consoantes foram lidas. Imprima as consoantes.
    """
    vogais = ['a', 'e', 'i', 'o', 'u']
    lista = []
    j = 0
    for i in range(10):
        caracter = input('Digite um caracter: ')
        caracter = caracter.lower()
        if caracter in vogais:
            pass
        else:
            lista.append(caracter)
            j += 1
    print(f'Foram inseridas {j} consoantes, são elas {lista}')


def questao11():
    """
     Faça um programa que leia 15 números inteiros e armazene-os em uma lista NUMEROS.
     Armazene os números
     pares na lista PAR e os números ímpares na lista IMPAR. Imprima os três vetores.
    """
    numeros = []
    par = []
    impar = []
    for i in range(10):
        numero = int(input('Digite um número: '))
        numeros.append(numero)
        if numero % 2 == 0:
            par.append(numero)
        else:
            impar.append(numero)
    print(f'Os números digitados foram {numeros}\n'
          f'Dentre eles esses são pares {par} e estes são ímpares {impar}')


def questao12():
    """
    Elabore um programa que efetue a leitura de quatro notas reais de10 alunos,
    calcule e armazene em uma lista,
    a média de cada aluno, imprima o número de alunos com média maior ou igual a 7.0.
    """
    lista = []
    k = 0
    for i in range(1, 11):
        soma = 0
        for j in range(1, 5):
            nota = float(input(f'Digite a {j}ª nota do aluno "{i}\n'))
            soma = soma + nota
        media = soma / 4
        lista.append(media)
        if media >= 7:
            k += 1
    print(f'A média dos 10 alunos eh {lista} sendo {k} acima da média')


def questao13():
    """
    Faça um programa que carregue uma lista com os modelos
    de cinco carros (exemplo de modelos: FUSCA, GOL, VECTRA etc).
    Carregue uma outra lista com o consumo desses carros, isto é,
    quantos quilômetros cada um desses carros faz com um litro de combustível.
    Calcule e mostre:

    O modelo do carro mais econômico;
    Quantos litros de combustível cada um dos carros
    cadastrados consome para percorrer uma distância de
    1000 quilômetros e quanto isto custará, considerando
    um que a gasolina custe 2,25 o litro.
    Abaixo segue uma tela de exemplo. O disposição das
    informações deve ser o mais próxima possível ao exemplo.
    Os dados são fictícios e podem mudar a cada execução do programa.
    Relatório Final
        1 - SUV - 10.0 - 100.0 litros - R 399.0
        2 - IDEA - 12.0 - 83.3 litros - R 332.5
        3 - GOL - 10.0 - 100.0 litros - R 399.0
        4 - BMW - 20.0 - 50.0 litros - R 199.5
        5 - UNO - 2.0 - 500.0 litros - R 1995.0
        O menor consumo é do BMW.

    """
    carros = ['Fusca', 'Gol', 'Vectra', 'Uno', 'Amarok']
    consumo = [20.0, 18.0, 9.5, 15.0, 5.7]
    economico = 9999
    j = 0
    for i in consumo:
        print(f'{j + 1}-{carros[j]} - {i} - {round(1000 / i, 1)} litros - R${round(1000 / i * 2.25, 1)}')
        if i < economico:
            economico = i
            carro = j
        j += 1
    print(f'O menor consumo é do {carros[carro]}')
    
    
# Main Program
# Veja o enunciado:
help(questao13())
# Chame determinadas funcoes atraves de:
questao13()