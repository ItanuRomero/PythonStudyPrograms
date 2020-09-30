"""Questão 3. Recriar o jogo da forca. Utilize sua criatividade, arquivos, funções, módulos, etc."""


def inserir_palavra():
    palavra_input = str(input('Digite uma palavra: ')).strip()
    return palavra_input


def inserir_dica():
    dica_usuario = str(input('Adicione uma dica ')).strip()
    return dica_usuario


def tentativa_usuario():
    letra_input = str(input('Chute uma letra: '))
    return letra_input


tentativas = 0
palavra = inserir_palavra()
palavra_em_lista = []

for letra in palavra:
    palavra_em_lista.append(letra)

dica = inserir_dica()

print('Passe para o outro jogador')
input('Aperte qualquer tecla para continuar...')
print(f'A dica e: {dica}')
while True:
    palpite = tentativa_usuario()
    if palpite in palavra:
        print(f'Acertou, a letra {palpite} esta na palavra, veja!\n')
        for letras in palavra_em_lista:
            if letras == palpite:
                print(letras, end='')
                palavra_em_lista.remove(letras)
            else:
                print(end='_')
        print()
        if not palavra_em_lista:
            print('Vc conseguiu, parabens!')
            break
    else:
        print('Errou! A letra digitada nao esta na palavra!')
        tentativas += 1
    if tentativas > 5:
        print('Acabaram suas chances!')
        break

print('Recomece para jogar novamente!')
