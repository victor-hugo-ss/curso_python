"""
Tipo de tipagem = Dinâmica / Forte
str -> string -> Texto
Strings são textos que estão dentro de aspas simples ou duplas
"""
# Aspas simples
print('Isso é uma string')

# Aspas duplas
print("Isso também é uma string")

# Escapando aspas
print('Isso é uma string com aspas simples \' dentro dela')

# raw string
print(r'Isso é uma string com uma barra n \n dentro dela')

# aspas duplas dentro de aspas simples
print('Isso é uma string com aspas duplas " dentro dela')

# Tipos int e float
# int -> inteiro -> Números inteiros
# O tipo int representa qualquer número positivo ou negativo.
# int sem sinal = somente positivos
# int com sinal = positivos e negativos
print(10)      # int
print(-10)     # int
print(0)       # int

# float -> real/ponto flutuante -> Números reais
# O tipo float representa qualquer número positivo ou negativo com ponto flutuante
# float sem sinal = somente positivos
# float com sinal = positivos e negativos
print(10.5)    # float
print(-10.5)   # float
print(0.0)     # float

# A funcão type mostra o tipo do dado
# inferiu ao valor
print(type('Isso é uma string'))  # <class 'str'>
print(type(10))                   # <class 'int'>
print(type(10.5))                 # <class 'float'>

# Tipo de dado bool (Boolean)
# bool -> Booleano -> True ou False
# O tipo bool representa valores lógicos
# Existem várioa operadores para "questionar"
# Dentre eles o igualdade ==
# Questiona se um valor é igual ao outro
print(10 == 10)   # bool
print(10 == 11)   # bool
print(type(10 == 10))  # <class 'bool'>
print(type(10 == 11))  # <class 'bool'>

# conversão de tipos, coercão
# type convertion, type casting, coercion
# converter um tipo em outro
# tipos imutáveis e primitivos:
# str, int, float, bool
print(int(1), type(int('1')))       # converte str em int
print(float('1') + 1)
print(bool(' '))        # str com espaço é True
print(str(11) + 'b')