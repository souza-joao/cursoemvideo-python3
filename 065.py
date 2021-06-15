num = cont = soma = maior = menor = 0
sn = 'S'
while sn in 'Ss':
    num = int(input('Digite um número : '))
    sn = str(input('Quer continuar? [S/N] ')).upper().strip()
    cont += 1
    soma += num
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
média = soma / cont
print('Acabou!')
print('A média dos números digitados é {:.1f}'.format(média))
print('O maior número digitado foi {} e o menor número digitado foi {}'.format(maior, menor))
