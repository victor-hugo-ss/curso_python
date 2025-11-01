# Operadores Aritméticos em Python
adicao = 5 + 3
print("Adição: 5 + 3 =", adicao)

subtracao = 10 - 4
print("Subtração: 10 - 4 =", subtracao)

multiplicacao = 7 * 6
print("Multiplicação: 7 * 6 =", multiplicacao)

divisao = 20 / 5.5
print("Divisão: 20 / 5.5 =", divisao)

divisao_inteira = 20 // 2.2
print("Divisão Inteira: 20 // 2.2 =", divisao_inteira)

exponenciacao = 3 ** 4
print("Exponenciação: 3 ** 4 =", exponenciacao)

modulo = 22 % 7 # Resto da divisão de 22 por 7
print("Módulo: 22 % 7 =", modulo)

# concatenação de strings usando o operador +
# Repetição de strings usando o operador *

concatenacao = "Olá, " + "mundo!"
print(concatenacao)

repeticao = "Python! " * 3
print(repeticao)

# Precedência dos operadores
# 1. Parênteses ()
# 2. Exponenciação (**)
# 3. Multiplicação (*), Divisão (/), Divisão Inteira (//), Módulo (%)
# 4. Adição (+), Subtração (-)
resultado = 3 + 5 * 2 ** 2 - (4 / 2)
print("Resultado da expressão 3 + 5 * 2 ** 2 - (4 / 2) =", resultado)

# Exercício prático

# Luiz Otávio tem 1.80m de altura e pesa 90kg.
# Qual é o IMC dele? (IMC = peso / (altura * altura))

nome = "Luiz Otávio"
altura = 1.80
peso = 90

imc = peso / (altura * altura)
print(f"O IMC de {nome} é: {imc:.2f}")