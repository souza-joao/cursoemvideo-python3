print('Vamos formar uma P.A')
print('=-=' * 8)
termo = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão: '))
contar = 0
continuar = 0
v = 10
while contar < v:
    print(f'{termo} ->', end=' ')
    termo += razão
    contar += 1
    if contar == v:
        print('Pausa')
        continuar = int(input('Quantos termos a mais você quer que seja calculado? '))
        v = contar + continuar
print(f'Ao todo foram {contar} termos mostrados.\nFim!')
