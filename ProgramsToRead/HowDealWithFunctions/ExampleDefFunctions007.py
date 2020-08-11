"""
Exercício Python 105: Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:

- Quantidade de notas
- A maior nota
- A menor nota
- A média da turma
- A situação (opcional)

Adicione também as docstrings dessa função para consulta pelo desenvolvedor.
"""
def notas(*num, situacao=False):
    """
    Recebe varias notas e retorna o boletim com a quantidade de notas,
    maior e menor, a media, e se caso quiser, a situacao.
    :param num: recebe uma, varias ou nenhuma nota.
    :param situacao: mostra a situacao do boletim (opcional)
    :return: retorna o boletim.
    """
    boletim = {
        'quantidade': len(num),
        'maior': max(num),
        'menor': min(num),
        'media': sum(num) / len(num)
    }
    if situacao:
        if boletim['media'] >= 7:
            boletim['situacao'] = 'Boa'
        elif boletim['media'] >= 5:
            boletim['situacao'] = 'Razoavel'
        else:
            boletim['situacao'] = 'Ruim'
    print('~' * 40)
    return boletim


# MainProgram
resposta = notas(7, 8, 9, situacao=True)
print(resposta)
# help(notas)
