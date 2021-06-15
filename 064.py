num = soma = cont = 0
num = int(input('Digite um número [Só para quando 999]: '))
while num != 999:
    cont += 1
    soma += num
    num = int(input('Digite um número [Só para quando 999]: '))
print('Acabou! Foram digitados {} números e a soma entre eles é {}'.format(cont, soma))
