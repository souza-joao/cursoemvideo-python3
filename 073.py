times = ('Flamengo', 'Internacional', 'Atlético MG', 'São Paulo', 'Fluminense', 'Grêmio',
'Palmeiras', 'Santos', 'Athletico PR', 'RB Bragantino', 'Ceará', 'Corinthians', 
'Atlético GO', 'Bahia', 'Sport', 'Fortaleza', 'Vasco', 'Goiás', 'Curitiba', 'Botafogo')
print(times[0:5])
print('=-' * 30)
print(times[16:20])
print('=-' * 30)
print(sorted(times))
print('=-' * 30)
'''for pos, c in enumerate(times):
    if c == 'Corinthians':
        print(f'O {c} está na posição {pos + 1}.')'''
print(f'O Corinthians está na {times.index("Corinthians") + 1}ª posição')
