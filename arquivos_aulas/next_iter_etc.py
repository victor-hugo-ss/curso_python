"""
Iterável -> str, range, etc
Iterador -> Quem sabe entregar um valor por vez
next -> Me entregue o próximo valor
iter -> Me entregue seu iterador
"""

texto = 'Victor' #Iterável
iteratador = iter(texto)

while True:
    try:
        letra = next(iteratador)
        print(letra)
    except StopIteration:
        break

for letra in texto:
    print(letra)