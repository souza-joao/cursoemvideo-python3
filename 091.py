from time import sleep
from random import randint
from operator import itemgetter
d = {'Jogador 1': randint(1, 6), 'Jogador 2': randint(1, 6), 'Jogador 3': randint(1, 6), 'Jogador 4': randint(1, 6)}
ranking = []
for k, v in d.items():
    print(f'O {k} tirou {v} no dado.')
    sleep(1)
ranking = sorted(d.items(), key=itemgetter(1), reverse=True)
print('-=' * 30)
print('  ==RANKING DOS JOGADORES==')
for i, v in enumerate(ranking):
    print(f'  {i+1}º lugar: {v[0]} com {v[1]}.')
