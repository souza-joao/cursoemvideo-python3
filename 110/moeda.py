def metade(n=0, formato=False):
    res = n / 2
    return res if formato is False else moeda(res)


def dobro(n=0, formato=False):
    res = n * 2
    return res if formato is False else moeda(res)


def aumentar(n=0, taxa=0, formato=False):
    """
    -> Calcula o aumento de determinado preco,
    restorna o resultado com ou sem formatacao.
    :param n: valor que se quer reajustar.
    :param taxa: Qual é a taxa a aumentar.
    :param formato: quer a saida formatada sim ou nao?
    :param return: retorna o resultado com ou sem formatacao.
    """
    res = n + (n * taxa/100)
    return res if formato is False else moeda(res)


def diminuir(n=0, taxa=0, formato=False):
    res = n - (n * taxa/100)
    return res if formato is False else moeda(res)
    

def moeda(n=0, moed='R$'):
    return f'{moed}{n:.2f}'.replace('.', ',')
    

def resumo(n=0, taxaa=50, taxar=10):
    print('-' * 31)
    print('Resumo do Valor'.center(31))
    print('-' * 31)
    print(f'Preço analizado: \t{moeda(n)}')
    print(f'Dobro do valor: \t{dobro(n, True)}')
    print(f'Metade do valor: \t{metade(n, True)}')
    print(f'{taxaa}% de aumento: \t{aumentar(n, taxaa, True)}')
    print(f'{taxar}% de redução: \t{diminuir(n, taxar, True)}')
    print('-' * 31)