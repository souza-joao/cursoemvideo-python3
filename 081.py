val = []
cont = 0
while True:
    val.append(int(input('Digite um número: ')))
    val.sort(reverse=True)
    cont += 1
    sn = ' '
    while sn not in 'NS':
        sn = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if sn == 'N':
        break
print(f'Foram digitados {cont} números.')
print(f'Os valores digitados em ordem decrescente são {val}.')
if 5 in val:
    print(f'O valor 5 na posição {val.index(5)}.')
else:
    print('O 5 não foi digitado.')
