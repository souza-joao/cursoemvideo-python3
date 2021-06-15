sexo = str(input('Digite o seu sexo: [ M/F ] ')).strip().upper()[0]
while sexo not in 'MF':
    sexo = str(input('Dado inválido! Digite o seu sexo: [ M/F ] ')).upper().strip()[0]
print(f'Sexo {sexo} registrado. ')