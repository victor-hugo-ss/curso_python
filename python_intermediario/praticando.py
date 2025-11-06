perguntas = [
    {
        'pergunta': 'Quanto é 2 + 2?',
        'Opções': ['1', '2', '4', '5'],
        'Resposta': '4'
    },
    {
        'pergunta': 'Quanto é 5 * 5?',
        'Opções': ['25', '55', '10', '51'],
        'Resposta': '25'
    },
    {
        'pergunta': 'Quanto é 10 / 2?',
        'Opções': ['4', '5', '2', '1'],
        'Resposta': '5'
    }
]

qtd_acertos = 0

for item in perguntas:
    print(f'pergunta:', item['pergunta'])
    print()

    opcoes = item['Opções']
    for i, opcao in enumerate(opcoes):
        print(f'{i})', opcao)

    
    entrada = input('\nDigite uma opção: ')

    entrada_int = None
    qtd_opcoes = len(opcoes)
    acertou = False

    if entrada.isdigit():
        entrada_int = int(entrada)

    if entrada_int is not None:
        if entrada_int >= 0 and entrada_int < qtd_opcoes:
            if opcoes[entrada_int] == item['Resposta']:
                acertou = True
        
    if acertou:
        qtd_acertos += 1
        print('\nAcertou! 👍\n')
    else:
        print('\nErrou! ❌\n')
    
print(f'Você acertou: {qtd_acertos}')
print('de', len(perguntas), 'perguntas.\n')