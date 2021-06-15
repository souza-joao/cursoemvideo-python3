def área(larg, comp):
    a = larg * comp
    print(f'A área do terreno é de {a:.2f}m².')
    

#PROGRAMA PRiNCIPAL
l = float(input('Largura (m): '))
c = float(input('Comprimento (m): '))
área(l, c)
