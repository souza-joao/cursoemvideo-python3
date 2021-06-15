L1 = float(input('Quanto mede um dos lados da parede?'))
L2 = float(input('Quanto mede o outro lado da parede?'))
A = L1 * L2
t = A / 2
print('A área é de {:.2f}m² e será preciso {:.2f}L de tinta para pintar a parede.'.format(A, t)) 
