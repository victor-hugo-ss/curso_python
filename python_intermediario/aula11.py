"""
Métodos úteis dos dicionários em Python
len - quantas chaves
keys - iterável com as chaves
values - iterável com os valores
items - iterável com as chaves e valores
setdefalt - adiciona uma cópia rasa (shallow copy)
get - obtém uma chave
pop - Apaga um item com a chave especificada (del)
popitem - apaga o último item adicionado
update - atualiza um dicionário com outro
"""
import copy

pessoa = {
    'nome': 'Victor',
    'sobrenome': 'Silva'
}

# pessoa.setdefault('idade', 0)
# print(len(pessoa))
# print(list(pessoa.keys()))
# print(list(pessoa.values()))
# print(list(pessoa.items()))

# Shallow copy vs Deep copy em dados mutáveis em Python
"""
d1 = {
    'c1': 1,
    'c2': 2,
    'l1': [0, 1, 2]
}

d2 = copy.deepcopy(d1)

d2['l1'][1] = 9999
d2['c1'] = 100

print(d1)
print(d2)
"""

p1 = {
    'nome': 'Victor',
    'idade': 24
}

# print(p1.get('nome'))
# nome = p1.pop('nome')
# print(nome)
# print(p1)

# ultima_chave = p1.popitem()
# print(ultima_chave)
# print(p1)

# p1.update({
#     'nome': 'novo nome',
#     'idade': 26,
#     'sobrenome': 'Silva'
# })

# p1.update(nome='novo valor', sobrenome='Silva', idade=25)
tupla = ('nome', 'novo valor'), ('sobrenome', 'Silva')
p1.update(tupla)
print(p1)