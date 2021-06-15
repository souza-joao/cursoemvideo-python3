print('-='  * 20)
print('\033[35mVamos analizar os possíveis triângulos.\033[m')
print('-=' * 20)
print('\033[35mInforme a medida de três retas:\033[m\n ')
r1 = float(input('Digite o valor da primeira: '))
r2 = float(input('Digite o valor da segunda: '))
r3 = float(input('Digite o valor da terceira: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\033[35mEstas medidas formam um triâmgulo\033[m ', end='')
    if r1 == r2 == r3:
        print('\033[35mEquilátero\033[m.')
    elif r1 == r2 != r3 or r2 == r3 != r1 or r3 == r1 != r2:
        print('\033[35mIsósceles\033[m.')
    else:
        print('\033[35mEscaleno\033[m.')
else:
    print('\033[31mEstas medidas NÃO PODEM FORMAR UM TRIÂNGULO.\033[m')
