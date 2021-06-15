num = (int(input('Digite um número: ')),
int(input('Digite um número: ')),
int(input('Digite um número: ')),
int(input('Digite um número: ')),)
print(f'O número 9 apareceu {num.count(9)} vez(es).')
if 3 in num:
    print(f'O número 3 aparece na {num.index(3) + 1}ª posição.')
else:
    print('Você não digitou o número 3.')
print('Os números pares foram ', end='')
for c in num:
    if c % 2 == 0:
        print(c, end=' ')
'''n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
n3 = int(input('Digite outro número: '))
n4 = int(input('Digite mais um número: '))
tup = (n1, n2, n3, n4)
print(f'O número 9 apareceu {tup.count(9)} vezes.')
print('-' * 60)
if tup.count(3) > 0:
    print(f'O número 3 está na posição {tup.index(3) + 1}.')
else:
    print(f'O número 3 não foi digitado.')
print('-' * 60)
print('Os valores pares foram ', end='')
if tup[0] % 2 == 0:
    print(f'{tup[0]} ', end='')
if tup[1] % 2 == 0:
    print(f'{tup[1]} ', end='')
if tup[2] % 2 == 0:
    print(f'{tup[2]} ', end='')
if tup[3] % 2 == 0:
    print(f'{tup[3]}')'''