"""
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma contagem
regressiva começando de 10

Exemplo: 746.824.890-70 (746824890)
    10  9  8  7  6  5  4  3  2
*   7   4  6  8  2  4  8  9  0
    ---------------------------
    70  36 48 56 12 20 32 27 0

Somar todos os resultados:
70 + 36 + 48 + 56 + 12 + 20 + 32 + 27 + 0 = 301
multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado for maior que 9:
    resultado = 0
contrário disso:
    resultado é o valor da conta

O primeiro dígito do CPF é 7
"""

cpf_numeros = "03310131262"
numeros = cpf_numeros[:9]
multiplicador = 10
soma = 0

for n in numeros:
    soma += int(n) * multiplicador
    multiplicador -= 1

resto_divisao = soma % 11
resto_divisao = 11 - resto_divisao if resto_divisao >= 2 else 0
novo_cpf_numeros = numeros + str(resto_divisao)

novo_multi = 11
nova_soma = 0

for n in novo_cpf_numeros:
    nova_soma += int(n) * novo_multi
    novo_multi -= 1

n_resto_divisao = nova_soma % 11
n_resto_divisao = 11 - n_resto_divisao if n_resto_divisao >= 2 else 0
novo_cpf_numeros = novo_cpf_numeros + str(n_resto_divisao)

cpf_formatado = '{}.{}.{}-{}'.format(novo_cpf_numeros[:3], novo_cpf_numeros[3:6], novo_cpf_numeros[6:9], novo_cpf_numeros[9:])

if cpf_numeros == novo_cpf_numeros:
    print(f'CPF válido: {cpf_formatado}\n')
else:
    print('CPF inválido')