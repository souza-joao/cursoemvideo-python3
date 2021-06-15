from math import hypot
ca = float(input('Qual o valor do C.A?'))
co = float(input('O valor do C.O:'))
hi = hypot(co, ca)
print('A hipotenusa vale {:.2f}.'.format(hi))
