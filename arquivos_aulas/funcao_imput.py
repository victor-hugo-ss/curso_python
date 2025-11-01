# Função input em Python 
# Esta função solicita ao usuário que digite algo e retorna o valor inserido como uma string.

# Exemplo de uso:
nome = input("Qual é o seu nome? ")
idade = input("Qual a sua idade? ")
idade_int = int(idade)

print("Olá, {}!".format(nome))
print(f"Sua idade é: {idade_int}")