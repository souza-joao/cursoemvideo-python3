nome = str(input('Digite o teu nome completo:')).strip()
separa = nome.split()
print('O teu primeiro nome é {}'.format(separa[0]))
print('O teu último nome é {}'.format(separa[len(separa)-1]))
# len() vai me mostrar a quantidade de espaços
# como eu usei len(separa) me mostra os nomes (pq o separa = nome.split())
# o -1 no final p/ mostrar q eu quero o ultimo nome.
 