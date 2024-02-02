#Exercício - sistema de pergutas e respostas 

perguntas = [
    {
        'Pergunta': 'Quanto é 16-41 ?',
        'Opções': ['25', '-25', '-15', '15'],
        'Resposta': '4',
    },
    {
        'Pergunta': 'Quanto é 6! ?',
        'Opções': ['360', '120', '720', '560'],
        'Resposta': '720',
    },
    {
        'Pergunta': 'Quanto é 15/4 ?',
        'Opções': ['3.75', '3.25', '3.80', '3.70'],
        'Resposta': '3.75',
    },
]

quest = perguntas

for i in range(0,3):
    print(f"\n{quest[i]['Pergunta']}")
    print("\n"'Opções:')
    todos = perguntas[i]['Opções']
    for indice, valor in enumerate(todos):
        print(f'{indice}) {valor}')
    a = int(input("\n"'Escolha uma opção: '))
    if i == 0:
        if i == 0 and a == 1:
            print("\n"'Certa resposta!')
        else:
            print("\n"'Resposta incorreta!')
    if i == 1:
        if i == 1 and a == 2:
            print("\n"'Certa resposta!')
        else:
            print("\n"'Resposta incorreta!')
    if i == 2:
        if i == 2 and a == 0:
            print("\n"'Certa resposta!')
        else:
            print("\n"'Resposta incorreta!')
            


