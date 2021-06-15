num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 
'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
 'dezessete', 'dezoito', 'dezenove', 'vinte')
while True:
    while True:
        escolha = int(input('Escolha um número de 0 a 20: '))
        if 0 <= escolha <= 20:
            break 
        else:
            print('\033[31mOpção inválida!\033[m') 
    print(f'Você escolheu o número {num[escolha]}')
    sn = ' '
    while sn not in 'SN':
        sn = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if sn == 'N':
        break
