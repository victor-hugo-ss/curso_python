"""
Exercício 02
Crie funções que duplicam, triplicam e quadruplicam o valor recebido como parâmetro.
"""
def operacao(multiplicador):
    def operar(numero):
        return numero * multiplicador
    return operar

operacao1 = operacao(2)
print(operacao1(4))