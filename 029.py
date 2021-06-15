vel = float(input('Qual a velocidade do veículo em km/h?'))
if vel > 80:
    m = (vel - 80)*7
    print('Você foi multado. \nO valor da multa é de R${:.2f}'.format(m))
else:
    print('Você está dentro do limite de velocidade.')
    