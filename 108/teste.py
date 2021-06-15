import moeda_m as md

p = float(input('Digite um preço: R$ '))
print(f'O dobro de {md.virgula(p)} é {md.virgula(md.dobro(p))}')
print(f'A metade de {md.virgula(p)} é {md.virgula(md.metade(p))}')
tmax = int(input(f'Quer aumentar o {md.virgula(p)} em quntos porcentos? '))
print(f'O aumento de {md.virgula(p)} em {tmax}% é de {md.virgula(md.aumentar(p, tmax))}')
tmin = int(input(f'Quer diminuir o {md.virgula(p)} em quantos porcentos? '))
print(f'{md.virgula(p)} diminuido em {tmin}% é {md.virgula(md.diminuir(p, tmin))}')
