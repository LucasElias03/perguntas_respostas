perguntas = {
    'Pergunta 1': {
        'pergunta': 'Quanto é 2+2? ',
        'respostas': {'a': '5','b': '4','c': '2','d': '0'},
        'resposta_certa': 'b',
    },
    'Pergunta 2': {
        'pergunta': 'Quanto é 3*2? ',
        'respostas': {'a': '5','b': '4','c': '6','d': '0'},
        'resposta_certa': 'c',
    },
    'Pergunta 3': {
        'pergunta': 'Quanto é 5*5? ',
        'respostas': {'a': '5','b': '4','c': '6','d': '10'},
        'resposta_certa': 'd',
    },
    'Pergunta 4': {
        'pergunta': 'Quanto é 1+1? ',
        'respostas': {'a': '2','b': '4','c': '6','d': '0'},
        'resposta_certa': 'a',
    }
}

qnt_resposta = 0
for pk, pv in perguntas.items():
    print(f'{pk}: {pv["pergunta"]}')

    print('Respostas: ')

    for rk, rv in pv['respostas'].items():
        print(f'[{rk}]: {rv}')

    resposta_usuario = input('Sua resposta: ')

    if resposta_usuario == pv['resposta_certa']:
        print('!!! VOCÊ ACERTOU !!!')
        qnt_resposta = qnt_resposta + 1
    else:
        print('!!! VOCÊ ERROU !!!')

    print()

qnt_pergunta = len(perguntas)
porcentagem = qnt_resposta / qnt_pergunta * 100

print(f'Você acertou {qnt_resposta} respostas.')
print(f'Sua porcentagem de acerto foi {porcentagem}%. ')
