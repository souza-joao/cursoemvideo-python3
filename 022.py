nome = str(input('Qual é o teu nome? ')).strip() # .strip() é para tirar os espaços inúteis. 
print('Analizando...')
print('O teu nome em letras maiúsculas fica: {}'.format(nome.upper()))
print('O teu nome em letras minusculas fica: {}'.format(nome.lower()))
# O len() mostraráquantos espaços tem o nome, enquanto o .count() vai contar quantos espaços em branco tem.
# .count() só irá contar os espaços pq foi usado (' ').
print('O teu nome tem {} letras.'.format(len(nome) - nome.count(' ')))
#print('O teu primeiro nome tem {} letras'.format(nome.find(' ')))
separa = nome.split()
print('O teu primeiro nome é {} e ele tem {} letras.'.format(separa[0], len(separa[0])))
