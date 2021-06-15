pa = ('python', 'programar', 'linguagem', 'aprender', 'notbook', 'teclado', 'vscode')
for p in pa:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
