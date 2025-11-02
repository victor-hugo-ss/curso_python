"""
Exercício
Exiba os índices da lista
0 maria
1 Helena
2 Luiz
"""

""" lista = ['Maria', 'Helena', 'Luiz']
indices = range(len(lista))

for i in indices:
    print(i, lista[i]) """

"""
Faça uma lista de compras com listas
O usuário deve ter a possibilidade de inserir, apagar e listar valores da sua lista
Não permita que o programa quebre com erros de índices inexistentes na lista
"""
lista = []
import os

while True:
    
    entrada = input('\nSelecione uma opação\n[i]nserir [a]pagar [l]istar: ')

    if entrada == 'i':
        inserir = input('Digite o produto para inserir: ')
        lista.append(inserir)
        os.system('cls')

    elif entrada == 'a':

        if len(lista) == 0:
            print('\nNada para apagar')
            continue
        
        apagar_str = input('Escolha um índice para apagar: ')

        try:
            indice = int(apagar_str)
            del lista[indice]
            print('\nProduto apagado!!')

        except IndexError:
            print('\nÍndice não existe na lista')
        except ValueError:
            print('\nPor favor, digite um número inteiro')
        except:
            print('\nErro desconhecido')
            
    elif entrada == 'l':

        os.system('cls')

        if lista == []:
            print('Nada para listar!!!')

        else:
            for a, b in enumerate(lista):
                print(a, b)  

    else:
        print('\nDigite uma opção válida!!!')