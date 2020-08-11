"""
Exercício Python 101: Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.
"""
def voto(ano_nascimento):
    """
    Recebe o ano de nascimento introduzido e calcula a idade do usuario,
    utilizando a data atual.
    :param ano_nascimento: recebe o ano de nascimento
    :return: idade e status do voto
    """
    from datetime import datetime
    idade = datetime.today().year - ano_nascimento
    if idade < 16:
        return f'Com {idade} anos: NAO VOTA'
    elif idade > 65 or 16 <= idade < 18:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATORIO.'


# MainProgram
print('-=' * 20)
ano = int(input('Ano de nascimento: '))
print(voto(ano))
