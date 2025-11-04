"""
Desempacotamento em chamadas de métodos e funções
"""

string = 'ABCD'
lista = ['Luiz', 'Mauro', 'Maria']
tupla = 'Python', 'é', 'legal'

a, b, c = lista
print(a, c)

print(*string)  # Desempacotando a string em caracteres individuais
print(*lista)   # Desempacotando a lista em elementos individuais
print(*tupla)   # Desempacotando a tupla em elementos individuais