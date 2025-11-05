"""
Escopo de funções em Python
Escopo significa o local onde aquele código pode atingir.
Existe o escopo global e o escopo local.
O escopo global é o escopo onde todo o código é alcançável.
O escopo local é o escopo onde apenas nomes do mesmo local
podem ser alcançados.
"""

def escopo():
    x = 10  # Variável local
    print(f'Valor de x dentro da função: {x}')

escopo()

# acessando a variavel y dentro da função
y = 20  # Variável global
def outra_funcao():
    print(f'Valor de y dentro da função: {y}')  # Acessa a variável global

outra_funcao()