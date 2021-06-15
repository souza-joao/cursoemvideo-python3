val = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n >= val[-1]:
        val.append(n)
        print('O valor foi adicionado ao final da lista...')
    else:
        pos = 0
        while pos < len(val):
            if n <= val[pos]:
                val.insert(pos, n)
                print(f'O valor foi adicionado na posição {pos}...')
                break
            pos += 1
print(f'Os valores digitados foram {val}')
