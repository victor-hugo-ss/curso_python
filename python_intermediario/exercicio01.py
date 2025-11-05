"""
Exercícios com Funções

Crie uma função que multiplica todos os argumentos
não nomeados recebidos
Retorne o total para uma variável e mostre o valor da variável.

Crie uma função que fala se o número é par ou ímpar.
Retorne se o número é par ou ímpar.
"""

def multi(*args):
    multiplicador = 1
    for i in args:
        multiplicador *= i
    return multiplicador

resultado = multi(5, 10, 10, 43, 32)
print(resultado)

def par_impar(numero):
    if numero % 2 == 0:
        return 'Par'
    return 'Ímpar'

numero = par_impar(13)
print(numero)