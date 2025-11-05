"""
args - Argumentos não nomeados
* - *args (empacotamento e desempacotamento)
"""
# Lembre-se de desempacotamento
""" x, y, *resto = 1, 2, 3, 4, 5
print(x, y, resto) """

def soma_numeros(*args):
    total = 0
    for numero in args:
        total += numero
    return total

# Testando a função soma_numeros com diferentes quantidades de argumentos
soma1 = soma_numeros(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(soma1)

soma2 = soma_numeros(5, 10, 15)
print(soma2)

soma3 = soma_numeros()
print(soma3)