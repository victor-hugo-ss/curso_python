# Operadores lógicos em Python
# and (e), or (ou), not (não)
# and: Retorna True se ambas as expressões forem verdadeiras.
# Se qualquer valor for considerado falso, o resultado será falsy.
# 0, 0.0, '' e False são considerados falsos em Python.
# Támbem existe o tipo None que é usado para representar um não valor.
entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')
senha_permitida = '123456'

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Você entrou no sistema')
else:
    print('Você saiu do sistema')

# or: Retorna True se qualquer expressão for verdadeira.
# Se todas as expressões forem falsas, o resultado será falsy.
# Exemplo:
idade = int(input('Informe sua idade: '))
if idade < 18 or idade > 65:
    print('Você não pode trabalhar')
else:
    print('Você pode trabalhar')

# not: Inverte o valor lógico da expressão.
# Se a expressão for True, o resultado será False e vice-versa.

usuario_ativo = False
if not usuario_ativo:
    print('Usuário inativo')
else:
    print('Usuário ativo')

# Operadores in e not in
# in: Verifica se um valor está presente em uma sequência (string, lista, tupla, etc.)
frase = 'Python é uma linguagem de programação'
if 'Python' in frase:
    print('A palavra Python foi encontrada na frase')

# not in: Verifica se um valor não está presente em uma sequência
if 'Java' not in frase:
    print('A palavra Java não foi encontrada na frase')