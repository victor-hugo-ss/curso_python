"""
split e join com list e str
split() -> divide uma string em uma lista de strings
join() -> une uma lista de strings em uma única string
"""

frase = "Olha só que, coisa mais linda"
# Usando split para dividir a frase em palavras
palavras = frase.split()
print(palavras)  # Saída: ['Olha', 'só', 'que', 'coisa', 'mais', 'linda']

palavras_1 = frase.split(',')
print(palavras_1)  # Saída: ['Olha só que', ' coisa mais linda']

frases_unidas = ' '.join(palavras_1)
print(frases_unidas)  # Saída: "Olha só que coisa mais linda"
