ger = []
ind = {}
idade = []
mulheres = []
maioridade = []
while True:
    ind['Nome'] = str(input('Nome: ')).strip().title()
    ind['Idade'] = int(input('Idade: '))
    ind['Sexo'] = ' '
    while True:
        ind['Sexo'] = str(input('Sexo: [M/F] ')).upper().strip()[0]
        if ind['Sexo'] not in 'FM':
            print('Opção inválida! Digite "F" para feminino ou "M" para masculino.')
        else:
            break
    if ind['Sexo'] == 'F':
        mulheres.append(ind['Nome'])
    idade.append(ind['Idade'])
    if ind['Idade'] >= sum(idade)/len(idade):
        maioridade.append(ind['Nome'])
    ger.append(ind.copy())
    ind.clear()
    while True:
        sn = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
        if sn not in 'SN':
            print('Opção inválida! Digite "S" para sim ou "N" para não.')
        else:
            break
    if sn == 'N':
        break
print('-=' * 30)
print(f'A) Foram cadastradas {len(ger)} pessoas.')
print(f'B) A média de idade é de {sum(idade)/len(idade):.2f}.')
print(f'C) Ao todo foram cadastradas {len(mulheres)} mulheres.\nSendo elas ', end='')
for c in range(0, len(mulheres)):
    print(f'{mulheres[c]}', end=' ')
    print()
print('D) As pessoas que tem idade acima da idade média são: ')
for c in range(0, len(maioridade)):
    print(f'{maioridade[c]}', end=' ')
  