def metade(n=0):
    res = n / 2
    return res


def dobro(n=0):
    res = n * 2
    return res


def aumentar(n=0, taxa=0):
    res = n + (n * taxa/100)
    return res


def diminuir(n=0, taxa=0):
    res = n - (n * taxa/100)
    return res
    

def virgula(n=0, moed='R$'):
    return f'{moed}{n:.2f}'.replace('.', ',')
    