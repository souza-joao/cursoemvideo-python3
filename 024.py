city = str(input('Digite o nome de uma cidade:')).strip()
print(city[:5].upper() == 'SANTO')
# '[:5]' foi p/ mostrar as 5 primeiras letras da cidade.
# .strip() foi p/ tirar os espaços desnecessários.
# .upper() vai corrigir p/ maiúsculo todas as letras do nome caso o usuario digite errado --
# -- por isso precisa de == SANTO; desta forma, havendo Santo por primeiro nome da cidade, --
# -- independente de como o usuario escreve-lo, o resultado será verdadeiro.