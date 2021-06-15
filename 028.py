from random import randint, choice
from time import sleep
print('_' * 40)
print('Vou pensar em um número entre 0 e 5.')
print('-' * 80)
print('PROCESSANDO...')
sleep(3)
print('pronto!')
sleep(0.5)
n = int(input('Em que número eu pensei? '))
print('-' * 80)
sleep(2)
randint(0, 5)
if n == randint(0, 5):
    print('Parabéns! vc acertou o número que o computador "pensou". {}'.format(n))
else:
    print('Que pena! Tente novamente mais tarde.')    
