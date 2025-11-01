import os
import random

lista_secreta = ["cachorro", "gato", "elefante", "leão", "tigre", "girafa", "zebra", "urso", "lobo", "macaco"]
palavra_secreta = random.choice(lista_secreta)

letras_acertadas = ''
tentativas = 0 

while True:

    letra_digitada = input('Digite uma letra: ')
    tentativas += 1

    if len(letra_digitada) > 1:
        print('Digite apenas uma letra.')
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada

    palavra_formada = ''
    
    for i in palavra_secreta:
        if i in letras_acertadas:
            palavra_formada += i
        else:
            palavra_formada += '*'
    
    print(palavra_formada)

    if palavra_formada == palavra_secreta:

        os.system('cls')
        print('VOCÊ GANHOU!!! PARABÉNS!\n')
        print('A palavra é:', palavra_secreta.upper())
        print(f'Número de tentativas: {tentativas}\n')

        palavra_secreta = random.choice(lista_secreta)
        letras_acertadas = ''
        tentativas = 0
