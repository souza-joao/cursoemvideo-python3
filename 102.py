def fatorial(num=0, show=False):
    """
    -> Calcula o fatorial de um número num.
    :param num: Número a ser calculado.
    :param show: (Opcional) mostra ou não a conta.
    :return : retorna o valor do fatorial de um número num.
    """
    f = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


print(fatorial(5, True))
help(fatorial)
