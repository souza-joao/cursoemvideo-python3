num = list()
while True:
    n = int(input('Digite um número: '))
    if n not in num:
        num.append(n)
        print('Valor adicionado com sucesso.')
    else:
        print('Valor já existente! Não será adicionado.')
    sn = ' '
    while sn not in 'sn':
        sn = str(input('Quer continuar? [S/N] ')).lower().strip()[0]
    if sn == 'n':
        break
print(f'Os valores digitados foram {sorted(num)}')

'''val = []                 # minha solução inicial #
cont = 0
while True:
    val.append(int(input('Digite um valor: ')))
    if val[cont] in val[:-1]:
        print('Valor já existente! Não será adicionado.')
        val.pop()
        cont -= 1
    else:
        print('Valor adicionado com sucesso.')
    sn = ' '
    while sn not in 'sn':
        sn = str(input('Quer continuar? [S/N] ')).lower().strip()[0]    
    if sn == 'n':
        break
    else:
        cont += 1
print(f'Os valores digitados foram {sorted(val)}.')'''
