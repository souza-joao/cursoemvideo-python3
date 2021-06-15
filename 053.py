'''# frase = str(input('Digite alguma frase ou alguma palavra qualquer: ')).upper().strip()
palavra = frase.split()
junto = ''.join(palavra)
print(f'A frase ao contrário fica {frase[::-1]}.')
if junto == junto[::-1]:
    print('E é um Palíndromo! ')
else:
    print('E não é um Palíndromo! ')         (Um dos modos de resolver este problema.)'''
frase = str(input('Digite alguma frase ou alguma palavra qualquer: ')).upper().strip()
palavra = frase.split()
junto = ''.join(palavra)
inverso = ''
for c in range(len(junto) - 1, -1, -1):
    inverso += junto[c]
print(f'O inverso de {junto} é {inverso}.')
if inverso == junto:
    print('Temos um palíndromo.')
else:
    print('Não temos um palíndromo.')
