print('Vamos criar uma P.A de 10 termos. \n')
r = int(input('Digite a razão: '))
t1 = int(input('Digite o primeiro termo: '))
cont = 0
while cont < 10 :
    print(f'{t1} ->', end=' ')
    t1 += r
    cont += 1
print('Fim!')
