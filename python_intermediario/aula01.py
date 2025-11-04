"""
Introdução às funções (def) em python
Funções são trechos de códigos usados para
replicar determinada ação ao longo do seu código.
Elas podem receber valores para parâmetros (argumentos)
e retornar um valor específico.
Por padrão, funções Python retornam None (nada).
"""

# Definição de uma função simples
def saudacao():
    print("Olá, seja bem-vindo(a) ao curso de Python!")

# Chamada da função
saudacao()

# Função com parâmetros
def saudacao_personalizada(nome):
    print(f"Olá, {nome}! Seja bem-vindo(a) ao curso de Python!")

# Chamada da função com argumento
saudacao_personalizada("Victor")
saudacao_personalizada("Juliana")

# Função com retorno de valor
def soma(a, b):
    return a + b

# Chamada da função e armazenamento do resultado
resultado = soma(5, 3)
print(f"A soma de 5 e 3 é: {resultado}")

# Função com valor padrão para parâmetro
def potencia(base, expoente=2):
    return base ** expoente

# Chamada da função com e sem o segundo argumento
potencia_quadrado = potencia(4)
potencia_cubo = potencia(4, 3)
print(f"4 ao quadrado é: {potencia_quadrado}")
print(f"4 ao cubo é: {potencia_cubo}")