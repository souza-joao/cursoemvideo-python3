print('=' * 20)
print('Vamos criar uma P.A.')
print('=' * 20)
r = int(input('Digite a razão desta P.A: '))
t1 = int(input('Digite o primeiro termo: '))
décimo = t1 + (11 - 1) * r
for c in range(t1, décimo, r ):
    print(f'{c}, ', end=' ')
print('Acabou!')