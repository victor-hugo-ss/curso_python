"""
Interpolação de Strings em Python
s - string
d e i - int (inteiro)
f - float (ponto flutuante)
x e X - int em hexadecimal (ABCDEF0123456789)
"""

nome = "Luiz"
preco = 1000.9421398
variavel = '%s o preço total foi R$%.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %04X' % (1500, 1500))