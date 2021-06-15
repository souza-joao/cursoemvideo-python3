def notas(* n, sit=False):
    """
        Função para analisar notas e situação de alunos:
    :param n: Necebe uma ou mais notas de alunos.
    :param sit: Valor opcional. Indica se deve ou não adicionar a situação.
    :param return: Dicionário com várias informações da situação dos alunos.
    """
    r = {}
    r['Total'] = len(n)
    r['Maior'] = max(n)
    r['Menor'] = min(n)
    r['Média'] = sum(n)/len(n)
    if sit == True:
        if r['Média'] < 5.5:
            r['Situação'] = 'Ruim.'
        elif 5.5 <= r['Média'] < 7:
            r['Situção'] = 'Regular.'
        elif r['Média'] >= 7:
            r['Situação'] = 'Bom.'
    return r


#Programa principal.
resp = notas(5.5, 7, 10, 9.2, sit=True)
print(resp)
help(notas)
