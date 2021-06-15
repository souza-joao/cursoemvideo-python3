print('Vamos formar a \033[32mSequência de Fibonacci\033[m.')
print('-' * 40)
fn = int(input('\nDigite o número que você quer ver a sua \033[32mSequência de Fibonacci\033[m: '))
print('-' * 40)
t1 = 0
t2 = 1
print(f'{t1} -> {t2}', end=' -> ')
cont = 3
while cont <= fn:
    cont += 1
    t3 = t1 + t2
    print(f'{t3}', end=' -> ')
    t1 = t2
    t2 = t3
print('Fim!')
