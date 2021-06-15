print('=' * 10, 'Lojas do João', '=' * 10)
preço = float(input('Digite o preço das compras: R$ '))
pagar = int(input('''Digite o meio de pagamento:
[ 1 ] À vista no dinnheiro/cheque:
[ 2 ] À vista no cartão: 
[ 3 ] Em 2x no cartão:
[ 4 ] 3x ou mais no cartão:
'''))
if pagar == 1:
    x = preço - (preço * 0.1)
    print('Você terá 10% de desconto. Valor a pagará é de R${:.2f}.'.format(x))
elif pagar == 2:
    x = preço - (preço * 0.05)
    print('Você terá 5% de desconto. Valor a pagar é de R${:.2f}.'.format(x))
elif pagar == 3:
    y = preço / 2
    print('Você terá de pagar 2x R${:.2f}. Preço total: R${:.2f}'.format(y, preço))
elif pagar == 4:
    z = int(input('Em quantas vezes deseja pagar?'))
    x = preço + (preço * 0.2)
    y = x / z
    print('(Juros de 20%). Você terá de pagar {}x de {:.2f}. Valor final será de R${}.'.format(z, y, x))
else:
    print('Opção inválida de pagamento.')