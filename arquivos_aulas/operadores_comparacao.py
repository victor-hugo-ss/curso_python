# Operadores de Comparação (relacionais) em Python
# > = maior que exemplo: 2 > 1 verdadeiro
# >= = maior ou igual a exemplo: 2 >= 2 verdadeiro
# < = menor que exemplo: 1 < 2 verdadeiro
# <= = menor ou igual a exemplo: 2 <= 2 verdadeiro
# == = igual a exemplo: 'a' == 'a' verdadeiro
# != = diferente de exemplo: 2 != 1 verdadeiro

# Exemplo de uso dos operadores de comparação
maior = 5 > 3
maior_ou_igual = 5 >= 5
menor = 2 < 4
menor_ou_igual = 3 <= 3
igual = 'python' == 'python'
diferente = 10 != 5

print(diferente)  # Saída: True

# Exercício prático

primeiro_valor = input('Digite o primeiro valor: ')
segundo_valor = input('Digite o segundo valor: ')

if primeiro_valor > segundo_valor:
    print(f'Primeiro valor: {primeiro_valor} é maior que o segundo valor {segundo_valor}')
elif primeiro_valor < segundo_valor:
    print(f'Segundo valor: {segundo_valor} é maior que o primeiro valor: {primeiro_valor}')
elif primeiro_valor == segundo_valor:
    print('Os valores são iguais')
else:
    print('A opção que você digitou não é válida')