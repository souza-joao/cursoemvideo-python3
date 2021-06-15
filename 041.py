from datetime import date
idade = int(input('Digite o ano em que você nasceu: '))
x = date.today().year - idade
print('O atleta tem ou fará {} anos.'.format(x))
if x < 9:
    print('Ele participará da categoria MIRIM.')
elif 9 < x < 14:
    print('Ele participará da categoria INFANTIL.')
elif 14 < x < 19:
    print('Ele participará da categoria JUNIOR.')
elif 19 < x < 25:
    print('Ele participará da categoria SENIOR.')
elif x > 25:
    print('Ele participará da categoria MASTER.')
