val = []
maior = menor = 0
for c in range(0, 5):
    val.append(int(input('Digite um valor: ')))
    if c == 0:
        maior = menor = val[c]
    else:
        if val[c] > maior:
            maior = val[c]
        if val[c] < menor:
            menor = val[c]
print(f'você dogitou os valores {val}.')
print(f'O maior valor digitado foi {maior} e está na(s) posição(ões) ', end='')
for i, v in enumerate(val):
    if v == maior:
        print(f'{i}...', end='')
print()
print(f'O menor valor digitado foi {menor} e ele está na(s) posição(ões) ', end='')
for i, v in enumerate(val):
    if v == menor:
        print(f'{i}...', end='')
print()
