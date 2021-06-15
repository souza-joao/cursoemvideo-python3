temp = []
per = []
maior = menor = 0
while True:
    temp.append(str(input('Nome: ')))
    temp.append(float(input('Peso: ')))
    if len(per) == 0:
        maior = menor = temp[1]
    else:
        if temp[1] > maior:
            maior = temp[1]
        elif temp[1] < menor:
            menor = temp[1]
    per.append(temp[:])
    temp.clear()
    sn = ' '
    if sn not in 'sn':
        sn = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if sn == 'N':
        break
print(f'Foram registradas {len(per)} pessoas.')
print(f'O maior peso registrado foi {maior}kg. Peso de ', end='')
for p in per:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
        print()
print(f'O menor peso foi {menor}kg. peso de ', end='')
for p in per:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')
        print()
