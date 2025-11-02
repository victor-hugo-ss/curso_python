"""
Introdução ao desempacotamento + tuples (Tuplas)
"""

nome1, nome2, nome3 = ['Maria', 'Helena', 'Luiz']
print(nome2)

nome1, *resto = ['Maria', 'Helena', 'Luiz']
print(nome1, resto)

_, _, nome, *resto = ['Maria', 'Helena', 'Luiz']
print(nome, resto)