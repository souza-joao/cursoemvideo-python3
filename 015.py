km = float(input('Qual foi a quilometragem andada? '))
dia = float(input('Quantos dias que o carro ficou alugado? '))
valor = (0.15 * km) + (60 * dia)
print('O valor total a ser pago é R${:.2f}'.format(valor))
