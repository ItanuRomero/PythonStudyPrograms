def validador_numerico(frase):
    while True:
        entrada = str(input(frase))
        if entrada.isnumeric():
            break
        print(f'Erro, o valor "{entrada}" nao eh numerico\n'
              f'Tente novamente:')
    valor_validado = float(entrada)
    return valor_validado
