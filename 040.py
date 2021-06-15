n1 = float(input('Digite a sua primeira nota: '))
n2 = float(input('Digite a sua segunda nota: '))
x = (n1 + n2) / 2
if x >= 7 and x <= 10:
    print('Parabéns! você passou. A sua média foi {:.1f} .'.format(x))
elif 5 <= x < 7:
    print('Estude mais! você ficou de recuperação. A sua méia foi {:.1f} .'.format(x))
elif x < 5 and x >= 0:
    print('Você não alcançou a média necessaria; está reprovado! A sua média foi {:.1f} .'.format(x))
else:
    print('ERRO!')