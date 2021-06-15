from time import sleep
c = ('\033[m',   #-- 0 -- Sem cor
'\033[0;30;41m', #-- 1 -- Vermelho
'\033[0;30;42m', #-- 2 -- Verde
'\033[0;30;43m', #-- 3 -- Amarelo
'\033[0;30;44m', #-- 4 -- Azul
'\033[0;30;45m', #-- 5 -- Roxo
'\033[7;30m',    #-- 6 -- Branco
)
def ajuda(h):
    titulo(f'Acessando o manual de comando \' {h} \' :', 4)
    print(c[6], end='')
    help(h)
    print(c[0], end='')
    sleep(1)


def titulo(msg, cor=0):
    tan = len(msg) + 4
    print(c[cor], end='')
    print('~' * tan)
    print(f'  {msg}')
    print('~' * tan)
    print(c[0], end='')
    sleep(0.5)


#Programa principal.
comando = ' '
while True:
    titulo('Sistema de ajuda PyHELP:', 2)
    comando = str(input('Função ou biblioteca > '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('Até Logo!', 1)
