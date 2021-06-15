from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
player = int(input('Qual a sua jogada? '))
print('JO')
sleep(0.5)
print('KEN')
sleep(0.5)
print('PÔ')
print('-=' * 14)
print('Você escolheu {}.'.format(itens[player]))
print('O computador escolheu {}.'.format(itens[computador]))
print('-=' * 14, '\n')
if computador == 0: # PEDRA
    if player == 0: 
        print('Empatou!')
    elif player == 1: 
        print('Você Ganhou!')
    elif player == 2: 
        print('Você Perdeu!')
    else:
        print('\033[31mOpção inválida!\033[m')
elif computador == 1: #PAPEL
    if player == 0: 
        print('Você Perdeu!')
    elif player == 1:
        print('Empatou!')
    elif player == 2:
        print('Você Ganhou!')
    else:
        print('\033[31mOpção inválida!\033[m')
elif computador == 2: #TESOURA
    if player == 0: 
        print('Você Ganhou!')
    elif player == 1:
        print('Você Perdeu!')
    elif player == 2:  
        print('Empatou!')
    else:
        print('\033[31mOpção inválida!\033[m')
        