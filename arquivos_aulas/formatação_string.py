# Formaração de Strings em Python
nome = "Ana"
idade = 28
altura = 1.65

# Usando f-strings (Python 3.6+)
mensagem = f'meu nome é {nome}, tenho {idade} anos de idade e minha altura é {altura:.2f}m.'
print(mensagem)

# Usando o método format()
mensagem_format = 'meu nome é {}, tenho {} anos de idade e minha altura é {:.2f}m.'.format(nome, idade, altura)
print(mensagem_format)