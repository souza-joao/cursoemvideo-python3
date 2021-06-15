from math import radians, sin, cos, tan
a = float(input('Insira o valor do ângulo: '))
s = sin(radians(a))
print('O seno de {}° é {:.2f}'.format(a, s))
c = cos(radians(a))
print('O cosseno de {}° é {:.2f}'.format(a, c))
t = tan(radians(a))
print('A tangente de {}° é {:.2f}'.format(a, t))
