from datetime import date
maior = menor = 0
for c in range(1, 8):
    nasc = int(input(f'Digite a data de nascimento da {c} pessoa: '))  
    x = date.today().year - nasc
    if x >= 18:
        maior += 1
    else:
        menor += 1
print(f'Temos {maior} pessoas maiores de idade e {menor} menores.')
