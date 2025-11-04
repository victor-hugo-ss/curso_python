"""
Tipo List em Python
Suporta vários valores de qualquer tipo.
Métodos úteis:
    - append(): Adiciona um item ao final da lista.
    - insert(): Insere um item em uma posição específica.
    - pop(): Remove do final ou de uma posição específica.
    - del: Remove um item por índice.
    - clear(): Remove todos os itens da lista.
    - extend(): Adiciona múltiplos itens de outra lista.
    - sort(): Ordena os itens da lista.
    + - concatena listas

Create Read Update Delete (CRUD)
Criar, Ler, Atualizar, Deletar = lista[i] (CRUD)
"""

listas = [1, 2, 3, 4, 5]

listas.append(6)          # Adiciona 6 ao final da lista
listas.insert(0, 0)      # Insere 0 na posição 0
listas.pop()              # Remove o último item (6)
del listas[0]            # Remove o item na posição 0 (0)
listas.clear()           # Remove todos os itens da lista

lista_a = [1, 2, 3]
lista_b = [4, 5, 6]
lista_c = lista_a + lista_b  # Concatena lista_a e lista_b

lista_d = lista_a.extend(lista_b)  # Adiciona os itens de lista_b em lista_a
lista_a.sort()            # Ordena os itens de lista_a
print(lista_a)
print(lista_c)