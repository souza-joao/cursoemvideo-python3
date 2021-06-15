from time import sleep
print('--=' * 20)
soun = str(input('\033[35mEstá precisando de um empréstimo para comprar uma casa?\033[m '))
print('--=' * 20)
if soun == 'sim':
    sleep(0.5)
    print('O senhor(a) precisará responder algumas perguntas.\n\nVamos iniciar o processo.\n ')
    sleep(1)
    casa = float(input('Qual o valor da casa que o senhor(a) deseja comprar? R$'))
    print(' ')
    sleep(0.5)
    salario = float(input('Qual é o seu salário atual? R$'))
    print(' ')
    sleep(0.5)
    tempo = float(input('Estamos quase lá.\n\nEm quantos anos o senhor(a) deseja pagar a casa? '))
    print('_' * 60)
    sleep(0.5)
    print('...\nVerificando os seus dados...')
    print(' ')
    x = casa / (tempo * 12)
    if x < (salario * 0.3):
        sleep(0.5)
        print('\033[32mParabéns! Foi aprovado o seu empréstimo.\nVocê terá de pagar por mês R${:.2f}.\033[m'.format(x))
    else:
        sleep(0.5)
        print('\033[31mInfelizmente o seu empréstimo não foi aprovado.\033[m')
else:
    print('Ok. Até a próxima!')