"""
Valores padrão para parâmetros em funções Python
Ao definir uma função, os parâmetros podem
ter valores padrão. Caso o valor não seja
enviado para o parâmetro, o valor padrão será
utilizado.
"""

# todo valor nomeado deve vir após os valores posicionais
def soma(x, y, z=None):
    if z is not None:
        print(f'Soma de {x=}, {y=} e {z=} |', x + y + z)
    else:
        print(f'Soma de {x=} e {y=} |', x + y)

# Chamadas da função
soma(2, 3)        
soma(2, 3, 4)
soma(x=5, y=10)
soma(y=7, x=3, z=1)