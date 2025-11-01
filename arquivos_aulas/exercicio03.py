frase = 'O python é uma linguagem de programação '\
    'multiparadigma. '\
    'Python foi criado por Guido van Rossum.'

i = 0
qtd_apareceu = 0
letra_apareceu = ''

while i < len(frase):
    letra_atual = frase[i]

    if letra_atual == ' ':
        i += 1
        continue

    qtd_letra = frase.count(letra_atual)

    if qtd_apareceu < qtd_letra:
       qtd_apareceu = qtd_letra
       letra_apareceu = letra_atual

    i += 1
print('A letra que apareceu mais vezes foi: "%s"' % letra_apareceu)
print(f'Apareceu: {qtd_apareceu} vezes')