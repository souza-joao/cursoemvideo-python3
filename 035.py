print('-='  * 20)
print('\033[35mVamos analizar os possíveis triângulos.\033[m')
print('-=' * 20)
print('\033[35mInforme a medida dde três retas:\n ')
r1 = float(input('Digite o valor da primeira:\033[m '))
r2 = float(input('\033[35m Digite o valor da segunda:\033[m '))
r3 = float(input('\033[35mDigite o valor da terceira:\033[m '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('\033[35mEstas medidas PODEM SIM FORMAR UM TRIÂNGULO.\033[m')
else:
    print('\033[35mEstas medidas NÃO PODEM FORMAR UM TRIÂNGULO.\033[m')
