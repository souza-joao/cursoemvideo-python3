frase = str(input('Escreva uma frase qualquer:')).lower().strip()
print('Existem {} letras "a" na fraze'.format(frase.count('a')))
print('A letra "a" começa ma posição {}'.format(frase.find('a') + 1))
# .rfind() procura a partir do lado direito.
print('A ultima vez que encontramos a letra "a" na frase é na posição {}'.format(frase.rfind('a') + 1))
# os outros erros do programa serão resolvidos nas proximas aulas.