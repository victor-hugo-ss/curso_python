"""
Operação Ternária em Python (condicional de uma linha)
<valor> if <condição> else <outro_valor>
"""
condicao = 10 > 5
variavel = 'Valor se verdadeiro' if condicao else 'Valor se falso'
print(variavel)  # Saída: Valor se verdadeiro

digito = 9
# novo_digito = digito if digito <= 9 else 0
novo_digito = 0 if digito > 9 else digito
print(novo_digito)  # Saída: 9