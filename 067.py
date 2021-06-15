n1 = 0
sn = 'Ss'
while True:
    n1 = int(input('Quer ver a tabuada de qual número? '))
    print('-' * 30)
    for c in range(1, 11):
        print(f'{n1} x {c} = {c * n1}')
    print('-' * 30)
    sn = str(input('Quer ver a tabuada de mais um número? [S/N] ')).strip().upper()
    if sn != 'S':
        break
print('Acabou!')
