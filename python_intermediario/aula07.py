"""
Higher Order Functions
Funções de primeira classe
"""
def saudacao(msg, nome):
    return f'Saudação: {msg}, {nome}!'

# Atribuindo a função a uma variável
#saudacao2 = saudacao
#print(saudacao2('Oi, tudo certo?'))

# Passando a função como parâmetro para outra função
def executa(funcao, *args):
    return funcao(*args)

f = executa(saudacao, 'Olá, você está aprendendo Python', 'Maria')
print(f)