mat = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
par = []
col3 = []
maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        mat[l][c] = int(input(f'Digite um número para [{l}, {c}]: '))
        if mat[l][c] % 2 == 0:
            par.append(mat[l][c])
        if c == 2:
            col3.append(mat[l][c])
        if l == 1:
            if c == 0:
                maior = mat[l][c]
            else:
                if mat[l][c] > maior:
                    maior = mat[l][c]
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{mat[l][c]:^5}]', end=' ')
    print()
print(f'A soma de todos os valores pares é {sum(par)}.')
print(f'A soma de todos os valores da 3ª coluna é {sum(col3)}.')
print(f'O maior valor da 2ª linha é {maior}.')
