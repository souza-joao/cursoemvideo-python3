tup = ('Lapes', 1.00, 'Borracha', 2.50, 'Apontador', 2.50, 'Caderno', 10.90, 'Estojo', 5.90, 'Mochila', 99.90, 'Regua', 3.50, 'Caneta', 1.50)
print('{:_^35}'.format('Papelaria do Jão'))
print('\n{:-^35}'.format('Produtos'))
for pos in range(0, len(tup)):
    if pos % 2 == 0:
        print(f'{tup[pos]:.<25}', end=' ')
    else:
        print(f'R${tup[pos]:>7.2f}')
