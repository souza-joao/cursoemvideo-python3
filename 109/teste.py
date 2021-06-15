import moeda as md

p = float(input('Digite um preço: R$ '))
print(f'O dobro de {md.moeda(p)} é {md.dobro(p, True)}')
print(f'A metade de {md.moeda(p)} é {md.metade(p, True)}')
tmax = int(input(f'Quer aumentar o {md.moeda(p)} em quntos porcentos? '))
print(f'O aumento de {md.moeda(p)} em {tmax}% é de {md.aumentar(p, tmax, True)}')
tmin = int(input(f'Quer diminuir o {md.moeda(p)} em quantos porcentos? '))
print(f'{md.moeda(p)} diminuido em {tmin}% é {md.diminuir(p, tmin, True)}')
