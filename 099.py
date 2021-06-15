from time import sleep
from random import randint
def maior(* num):
    print('-=' * 25)
    maior = cont = 0
    print('Analisando os valores...')
    for valores in num:
        print(valores, end=' ', flush=True)
        sleep(0.2)
        cont += 1
        if cont == 0:
            maior = valores
        else:
            if valores > maior:
                maior = valores
    print()
    print(f'Foram analisados {cont} valores. ')
    print(f'O maior valor foi {maior}.')


#Programa Principal
maior(randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9))
maior(randint(0, 9), randint(0, 9), randint(0, 9))
maior(randint(0, 9), randint(0, 9))
maior()
maior(randint(0, 9))
