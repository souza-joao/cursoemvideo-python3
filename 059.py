print('Escoha dois números inteiros.')
n1 = int(input('Digite o 1º número: '))
n2 = int(input('Digite o 2º número: '))
menu = 0
while menu != 5:
    menu = int(input('''escolha uma das opções abaixo:
    [ 1 ] p/ soma:
    [ 2 ] p/ multiplicação:
    [ 3 ] p/ mostrar o maior:
    [ 4 ] p/ escolhar novos números:
    [ 5 ] p/ sair do programa:
    '''))
    if menu == 1:
        print(f'A soma entre {n1} e {n2} é {n1 + n2}')
    elif menu == 2:
        print(f'A multiplicação entre {n1} e {n2} é {n1 * n2}')
    elif menu == 3:
        if n1 > n2:
            print(f'{n1} é maior que {n2}')
        elif n1 < n2:
            print(f'{n2} é maior que {n1}')
        else:
            print('Os dois valores digitados são iguais!')
    elif menu == 4:
        n1 = int(input('Digite o 1º número: '))
        n2 = int(input('Digite o 2º número: '))
    elif menu != 1 and menu != 2 and menu != 3 and menu != 4 and menu != 5:
        print('\033[31mOpção inválida! tente novamente.\033[m')
    print('=-=' * 20)
print('Fim!')
