from random import randint
print('-=' * 20)
print('{:^40}'.format('Mega Sena'))
print('-=' * 20)
n = int(input('Quantos jogos você quer fazer? '))
ms = []
m = []
for c in range(0, n):
    for i in range(0, 6):
        ms.append(randint(0, 60))
        ms.sort()
    m.append(ms[:])
    ms.clear()
for c in range(1, n+1):
    print(f'Jogo {c}: {m[c-1]}')
