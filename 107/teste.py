from moeda import dobro, metade, aumentar, diminuir
p = float(input('Digite um preço: R$ '))
print(f'O dobro de {p} é {dobro(p)}')
print(f'A metade de {p} é {metade(p)}')
tmax = int(input(f'Quer aumentar o {p} em quntos porcentos? '))
print(f'O aumento de {p} em {tmax}% é de {aumentar(p, tmax)}')
tmin = int(input(f'Quer diminuir o {p} em quantos porcentos? '))
print(f'{p} diminuido em {tmin}% é {diminuir(p, tmin)}')
