def ficha(a='<Desconhecido>', b=0):
    print('_' * 40)
    print(f'O jogador {a} fez {b} gol(s).')


print('_' * 40)
nome = str(input('Nome do jogador: ')).strip().title()
gol = str(input('Gols: '))
if gol.isnumeric():
    gol = int(gol)
else: 
    gol = 0
if nome == '':
    ficha(b = gol)
else:
    ficha(nome, gol)
