média = 0
nn = 0
maior = 0
quant = 0
for c in range(1, 5):
    nome = str(input(f'Digite o nome da {c}ª pessoa: ')).strip()
    idade = int(input(f'Digite a idade da {c}ª pessoa: '))
    sexo = int(input(f'''Digite o sexo da {c}ª pessoa:
    [ 1 ] p/ Masculíno:
    [ 2 ] p/ Feminíno:
    '''))
    média += idade
    if sexo == 2 and idade < 20:
        quant += 1
    if c == 1 and sexo == 1:
        maior = idade
        nn = nome
    else:
        if idade > maior and sexo == 1:
            maior = idade
            nn = nome
x = média / 4
print(f'O homem mais velho se chama {nn} e tem {maior} anos')
print(f'A média da idade de todas as pessoas acima é de {x:.1f} anos')
print(f'{quant} mulheres tem menos de 20 anos.')
