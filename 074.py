from random import randint
tup = (randint(0, 9), randint(0, 9), randint(0, 9), randint(0, 9))
for n in tup:
    print(n, end=' ')
print(f'\nO maior valor foi {max(tup)}')
print(f'O menor valor foi {min(tup)}')
