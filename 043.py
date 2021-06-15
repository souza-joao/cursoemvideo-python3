peso = float(input('Digite é o seu peso: (kg) '))
altura = float(input('Digite é a sua altura: (m) '))
imc = peso / altura**2
print('O seu imc é {:.1f}. Você está '.format(imc), end='')
if imc < 18.5:
    print('Abaixo do Peso.') 
elif 18.5 < imc < 25:
    print('no Peso Ideal.')
elif 25 < imc < 30:
    print('com Sobrepeso.')
elif 30 < imc < 40:
    print('Obeso.')
elif 40 < imc:
    print('na fase de Obesidade Mórbida.')
