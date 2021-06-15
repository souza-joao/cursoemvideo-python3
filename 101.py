def voto(nasc):
    from datetime import date
    idade = date.today().year - nasc
    if 65 > idade >= 18:
        return f'Com {idade} anos o voto é obrigatório!'
    elif idade >= 65  or 16 <= idade < 18:
        return f'Com {idade} anos o voto é opcional!'
    else:
        return f'Com {idade} anos não pode votar!'



print('_' * 30)
n = int(input('Em que ano você nasceu: '))
print(voto(n))
