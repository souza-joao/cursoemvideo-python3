from random import randint
from time import sleep
def sorteio(lista):
    print('Vamos sortear 5 valores. ', end='')
    for c in range(0, 5):
        n = randint(1, 10)
        lista.append(n)
        print(f'{n} ', end='', flush=True)
        sleep(0.3)
    print('Pronto!')

def somapar(lista):
    soma = 0
    for valor in lista:
        if valor % 2 == 0:
            soma += valor
    print(f'A soma dos valores pares de {lista} é {soma}.')


val = []
sorteio(val)
somapar(val)
