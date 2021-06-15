print('=' * 30)
print('{:^30}'.format('BANCO DO JÃO'))
print('=' * 30)
valor = int(input('Qual o valor que você deseja sacar? R$'))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f'Foram retiradas {totced} cédulas de R${ced}.')
        if ced == 50:
            ced = 20
            totced = 0
        elif ced == 20:
            ced = 10
            totced = 0
        elif ced == 10:
            ced = 1
            totced = 0
        elif total == 0:
            break
