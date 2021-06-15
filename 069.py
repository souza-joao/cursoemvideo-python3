cont = s = i = s1 = 0
while True:
    cont += 1
    print('-=' * 20)
    print(f'Vamos fazer o cadastro da {cont}ª pessoa.')
    print('-=' * 20)
    idade = int(input('\nIdade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('sexo: [ M / F ] ')).upper().strip()[0]
    if idade >= 18:
        i += 1
    if sexo == 'M':
        s += 1
    if sexo == 'F' and idade < 20:
        s1 += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('\nQuer cadastrar mais alguém? [ S / N ] ')).upper().strip()[0]
    if continuar == 'N':
        break
print('-=' * 20)
print(f'{i} Pessoas cadastradas tinham mais de 18 anos.')
print(f'{s} Homens foram cadastrados.')
print(f'{s1} Mulheres que foram cadastradas tinham menos de 20 anos.')
