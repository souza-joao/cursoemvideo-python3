lista = []
listpar = []
listimpar = []
while True:
    n = int(input('Digite um número: '))
    lista.append(n)
    if n % 2 == 0:
        listpar.append(n)
    else:
        listimpar.append(n)
    sn = ' '
    while sn not in 'SN':
        sn = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if sn == 'N':
        break
print(f'Os valores digitados foram {lista}.')
print(f'Os valores pares foram {listpar}.')
print(f'Os valores impares foram {listimpar}.')
