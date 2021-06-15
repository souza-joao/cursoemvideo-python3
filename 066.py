n = cont = soma = 0
while True:
    n = int(input('Digite o número: '))
    if n == 999:
        break
    soma += n
    cont += 1
print(f'Acabou!\nForam digitados {cont} números e a soma entre eles é {soma}.')
