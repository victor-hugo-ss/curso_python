"""
Tipo tupla - uma lista imutável
"""

nomes = ['Maria', 'Helena', 'Luiz'] # Lista
nomes1 = 'Maria', 'Helena', 'Luiz' # Tupla
nomes1 = ('Maria', 'Helena', 'Luiz') # Tupla
print(nomes)

nomes = tuple(nomes) # Converte lista para tupla
print(nomes)