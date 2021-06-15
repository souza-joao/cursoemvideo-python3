player = dict()
gol = []
player['Nome'] = str(input('Nome: ')).strip().title()
partidas = int(input(f'Quantas partidas {player["Nome"]} jogou: '))
for c in range(1, partidas + 1):
    gol.append(int(input(f'Quantos gols {player["Nome"]} fez no {c}º jogo? ')))
player['Gols'] = gol[:]
player['Total de gols'] = sum(gol) 
print('-=' * 30)
print(player)
print('-=' * 30)
for k, v in player.items():
    print(f'  -O campo {k} recebe {v}.')
print('-=' * 30)
print(f'   O jogador {player["Nome"]} jogou {partidas} partidas')
for c in range(0, partidas):
    print(f'   == Na partida {c + 1}, fez {player["Gols"][c]} gols.==')
print(f'Foi um total de {sum(gol)} gols.')
