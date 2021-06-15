from time import sleep
dist = float(input('Qual é a distância em km do seu ponto de partida ao seu destino?'))
print('_' * 70)
print('Você está preste a iniciar uma viagem de {}km'.format(dist))
print('_' * 70)
sleep(2)
if dist <= 200:
    preço = dist * 0.5
else:
    preço = dist * 0.45
print('A sua passagem custa R${:.2f}'.format(preço))
