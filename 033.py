print('Escolha três números. ')
n1 = float(input('Digite o primeiro: '))
n2 = float(input('Digite o segundo: '))
n3 = float(input('Digite o terceiro: '))
menor = n1 
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3
print('O menor valor é {}.'.format(menor))
maior = n1 
if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3
print('O maior valor é {}.'.format(maior))
