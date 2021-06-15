salario = float(input('Qual é o seu salário atual? R$ '))
if salario >= 1250:
    aumento = salario + (salario * 0.1)
else:
    aumento = salario + (salario * 0.15)
print('O seu salario agora é R${:.2f}'.format(aumento))
