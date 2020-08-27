vogais = {
    'a': 0,
    'e': 0,
    'i': 0,
    'o': 0,
    'u': 0
}
texto = str(input('insira um texto: ')).strip().lower()
for letra in texto:
    if letra in 'a':
        vogais['a'] += 1
    elif letra in 'e':
        vogais['e'] += 1
    elif letra in 'i':
        vogais['i'] += 1
    elif letra in 'o':
        vogais['o'] += 1
    elif letra in 'u':
        vogais['u'] += 1
print(vogais)

