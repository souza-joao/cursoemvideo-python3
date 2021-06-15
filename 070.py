soma = cont = menor = b1 = 0
barato = ''
print('-' * 40)
print('{:^40}'.format('Lojão do Jão'))
print('-' * 40)
while True:
    produto = str(input('\nProduto: ')).strip().title()
    preço = float(input('Preço: R$'))
    soma += preço
    b1 += 1
    if preço >= 1000:
        cont += 1
    if b1 == 1 or preço < menor:
        menor = preço
        barato = produto
    seq = ' '
    while seq not in 'SN':
        seq = str(input('Quer continuar informando mais produtos? [ S/N ]\n')).strip().upper()[0]
    if seq == 'N':
        break
print('{:-^40}'.format('Fim do programa.'))
print(f'O preço total da compra foi de R${soma:.2f}.')
print(f'{cont} produtos custou(ararm) mais de R$1000.00')
print(f'O produto mais barato foi {barato} e custou R${menor:.2f}')
