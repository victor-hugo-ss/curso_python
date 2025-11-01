palavras = ["python", "asimov", "código", "web", "programação"]

maior_palavra = palavras[0]
menor_palavra = palavras[0]

for palavra in palavras:
    if len(palavra) > len(maior_palavra):
        maior_palavra = palavra
    if len(palavra) < len(menor_palavra):
        menor_palavra = palavra

print('A maior palavra é:', maior_palavra)
print('A menor palavra é:', menor_palavra)

#Segunda questão

numeros = [32, 10, 58, 30, 55, 12, 28, 51]
numeros.sort()
segundo_maior = numeros[-2]

print("O segundo maior valor da lista é:", segundo_maior)