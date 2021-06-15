num = int(input('Escolha um número inteiro: '))
print('Escolha a base de conversão. ')
n1 = int(input('''Digite
[ 1 ] para \033[32mBinário\033[m:
[ 2 ] para \033[36mOctal\033[m:
[ 3 ] para \033[35mHexadecimal\033[m:\n'''))
if n1 == 1:
    print('O número {} em \033[32mBinário\033[m é {}.'.format(num, bin(num) [2:]))
elif n1 == 2:
    print('O número {} em \033[36mOctal\033[m é {}.'.format(num, oct(num) [2:]))
elif n1 == 3:
    print('O número {} em \033[35mHxadecimal\033[m é {}.'.format(num, hex(num) [2:]))
else:
    print('\033[31mOpção inválida! Tente novamente mais tarde\033[m.')
