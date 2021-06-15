from random import randint, choice
from time import sleep
print('_' * 40)
print('Vou pensar em um número entre 0 e 10.\n')
print('PROCESSANDO...')
sleep(3)
print('pronto!')
sleep(0.5)
n = int(input('Em que número eu pensei? '))
print('-' * 80)
sleep(2)
x = randint(0, 10)  
cont = 0
while n != x:
    if n < x:
        n = int(input('EROOOOOOOOOOUUUUUUUUUUU! É um valor maior. Tente novamente: '))
        cont += 1
    else:
        n = int(input('EROOOOOOOOOOUUUUUUUUUUU! É um valor menor. Tente novamente: '))
        cont += 1
print(f'Parabéns, você acertou com {cont} jogadas! ')