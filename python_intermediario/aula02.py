"""
Argumentos nomeados e não nomeados em funções Python
Argumento nomeado tem nome com sinal de igual
Argumento não nomeado recebe apenas o argumento (valor)
"""

#definição da função
def soma(x, y):
    print(x + y)

# Argumentos não nomeados
soma(2, 3)

# Argumentos nomeados
soma(x=5, y=7)
soma(y=10, x=15)

# Mistura de argumentos nomeados e não nomeados
# Correto: o argumento não nomeado vem primeiro
soma(4, y=6)

# Incorreto: argumento nomeado não pode vir depois do não nomeado
# soma(x=8, 2)    
