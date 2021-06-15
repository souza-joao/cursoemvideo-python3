from random import randint
print('Vamos jogar IMPAR ou PAR:')
cont = 0
itens = ('Par', 'Impar')
while True:
    print('==' * 16)
    print('''Você deseja jogar para:
    [ 0 ] PAR
    [ 1 ] IMPAR''')
    ep = int(input('Qual a sua escolha? '))
    if ep == 0:
        ec = 1
    else:
        ec = 0
    print(f'\nVocê quer que de {itens[ep]}')
    print(f'E o computador quer que de {itens[ec]}\n')
    nc = randint(0, 9)
    np = int(input('Escolha um número inteiro: '))
    print(f'O computados escolheu {nc}\n')
    x = np + nc
    if x % 2 == 0:
        print('O resultado deu PAR.')
        if ep == 1:
            break
        else:
            cont += 1
    else:
        print('O resultado deu IMPAR.')
        if ep == 0:
            break
        else:
            cont += 1
print(f'Você obteve {cont} vitórias.')
