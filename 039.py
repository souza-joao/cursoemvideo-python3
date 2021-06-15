from datetime import date
sexo = int(input('''Qual é o seu sexo?
Digite:
[ 1 ] p/ Masculino.
[ 2 ] p/ Feminino. '''))
if sexo == 1:
    idade = int(input('digite o ano de seu nascimento: '))   
    x = date.today().year - idade
    if x > 18:
        y = x - 18
        print('''Você já passou da idade de alistamento por {} ano(s).
O seu alistamento foi em {}.'''.format(y, date.today().year - y))
    elif x < 18:
        y = 18 - x
        print('''Faltam {} ano(s) para você precisar se alistar.
O seu alistamento será em {}.'''.format(y, date.today().year + y))
    else:
        print('Você precisa se alistar este ano!')
elif sexo == 2:
    print('Você não é obrigada a se alistar no exército brasileiro.')
else:
    print('Opção invalida!')
    