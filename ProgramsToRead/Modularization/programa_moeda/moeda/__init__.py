def metade(valor, formatar=False):
    valor = valor / 2
    if formatar:
        valor = moeda(valor)
    return valor


def dobro(valor, formatar=False):
    valor *= 2
    if formatar:
        return moeda(valor)
    return valor


def aumentar(valor, porcentagem, formatar=False):
    aumenta = valor * (porcentagem / 100)
    valor += aumenta
    if formatar:
        return moeda(valor)
    return valor


def diminuir(valor, porcentagem, formatar=False):
    diminui = valor * (porcentagem / 100)
    valor -= diminui
    if formatar:
        return moeda(valor)
    return valor


def moeda(valor_em_reais):
    valor_final = f'R${valor_em_reais:.2f} '
    return valor_final


def resumo(valor, porcentagem1, porcentagem2):
    print(f'{"RESUMO":-^30}')
    print('-' * 30)
    print(f'Preco analisado:  {moeda(valor)}\n'
          f'Dobro do preco:   {dobro(valor, True)}\n'
          f'Metade do preco:  {metade(valor, True)}\n'
          f'{porcentagem1}% de aumento:   {aumentar(valor, porcentagem1, True)}\n'
          f'{porcentagem2}% de reducao:   {diminuir(valor, porcentagem2, True)}')
    print('-' * 30)
