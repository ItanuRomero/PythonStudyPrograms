# Questão 11. Construa uma função que receba uma data no formato DD/MM/AAAA 
# e devolva uma string no formato D de mes_por_extenso de AAAA. Opcionalmente, 
# valide a data e retorne NULL caso a data seja inválida. (Pesquisar sobre 
# expressão regular para resolver a questão para validar o texto por extenso.)

import re

def mes_por_extenso(data):
    x = re.search("\d{2}/\d{2}/\d{4}", data)

    if x:

        dia, mes, ano = data.split('/')
        if mes == "01":
            print(dia,"de Janeiro",ano)
        elif mes == "02":
            print(dia,"de Fevereiro",ano)
        elif mes == "03":
            print(dia,"de Março",ano)
        elif mes == "04":
            print(dia,"de Abril",ano)
        elif mes == "05":
            print(dia,"de Maio",ano)
        elif mes == "06":
            print(dia,"de Junho",ano)
        elif mes == "07":
            print(dia,"de Julho",ano)
        elif mes == "08":
            print(dia,"de Agosto",ano)
        elif mes == "09":
            print(dia,"de Setembro",ano)
        elif mes == "10":
            print(dia,"de Outubro",ano)
        elif mes == "11":
            print(dia,"de Novembro",ano)
        elif mes == "12":
            print(dia,"de Dezembro",ano)
        else:
            print('Mês inválido')
    else:
        print('Não esta em formato DD/MM/AAAA')
        
data = input("Data em formato DD/MM/AAAA\n")
mes_por_extenso(data)