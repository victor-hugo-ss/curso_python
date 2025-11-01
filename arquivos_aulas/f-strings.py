"""
Formatação básica de strings
s - string
d - int
f - float
.<número de digitos>f
x ou X - Hexadecimal
(Caracter)(><^)(quantidade)
> - esquerda
< - Direita
^ - centro
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a
"""

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}')
print(f'{variavel: ^10}')
print(f'{1000.2394874234343:0=+10,.2f}')