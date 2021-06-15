num = [[], []]
for c in range(1, 8):
    n = int(input(f'Digite o {c}º valor: '))
    if n % 2 == 0:
        num[0].append(n)
    else:
        num[1].append(n)
print(f'Todos os valores foram {num}')
print(f'Os valores ímpares são {sorted(num[1])}.')
print(f'Os valores pares são {sorted(num[0])}.')
