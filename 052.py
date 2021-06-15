tot = 0
n = int(input('Digite um número inteiro e veremos se este é ou não um número primo: '))
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[31m', end=' ')
        tot += 1
    else:
        print('\033[m', end=' ')
    print(f'{c}', end=' ')
print(f'\n\033[mO número {n} foi dividido {tot} vezes.', end=' ')
if tot == 2:
    print('Por isso ele é Primo')
else:
    print('Por isso ele não é primo')