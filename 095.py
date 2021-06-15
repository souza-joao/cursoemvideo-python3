player = dict()
gol = []
time = []
while True:
    player.clear()
    player['Nome'] = str(input('Nome: ')).strip().title()
    partidas = int(input(f'Quantas partidas {player["Nome"]} jogou: '))
    gol.clear()
    for c in range(1, partidas + 1):
        gol.append(int(input(f'Quantos gols {player["Nome"]} fez no {c}º jogo? ')))
    player['Gols'] = gol[:]
    player['Total de gols'] = sum(gol) 
    time.append(player.copy())
    while True:
        resp = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
        if resp in 'SN':
            break
        else:
            print('Erro! Digite "S" para sim ou "N" para não.')
    if resp == 'N':
        break
print('-=' * 30)
print('Cod ', end=' ')
for i in player.keys():
    print(f'{i:<15} ', end=' ')
print()
print('_' * 50)
for k, v in enumerate(time):
    print(f'{k:>3} ', end=' ')
    for d in v.values():
        print(f'{str(d):<15}', end=' ')
    print()
print('_' * 50)
while True:
    busca = int(input('Quer ver o desempenho de qual jogador? (999 para parar) '))
    if busca == 999:
        break
    if busca >= len(time):
        print('Erro! Jogador não encontrado.')
    else:
        print(f'  ==Levantamento Do Jogador {time[busca]["Nome"]}:==')
        for i, g in enumerate(time[busca]['Gols']):
            print(f'    No jogo {i+1} fez {g} gols.')
    print('_' * 50)
