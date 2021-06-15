notas = []
bolet = []
while True:
    notas.append(str(input('Nome: ')).title())
    notas.append(float(input('Nota 1: ')))
    notas.append(float(input('Nota 2: ')))
    bolet.append(notas[:])
    notas.clear()
    sn = ' '
    while sn not in 'SN':
        sn = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if sn == 'N':
        break
print('-=' * 30)
print('{:<5} {} {:>15}'.format('Nº', 'Nome', 'Média'))
print('_' * 30)
for l in range(0, len(bolet)):
        print(f'{l+1:<5} {bolet[l][0]:<15} {(bolet[l][2] + bolet[l][1])/2}')
print('_' * 30)
analize = str(input('Quer ver as nota de algum aluno? [S/N]: ')).upper().strip()[0]
if analize == 'S':
    while True:
        n = int(input('Mostrar as notas de qual aluno? [1, 2, 3, ..., n] '))
        print(f'As notas de {bolet[n-1][0]} foram {bolet[n-1][1], bolet[n-1][2]}')
        sn1 = ' '
        while sn1 not in 'SN':
            sn1 = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
        if sn1 == 'N':
            break
