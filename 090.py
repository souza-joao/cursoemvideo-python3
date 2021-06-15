dados = {}
dados['nome'] = str(input('Nome do aluno: ')).strip().title()
dados['média'] = float(input(f'Média de {dados["nome"]}: '))
if dados['média'] < 4:
    dados['situação'] = 'Reprovado'
elif 4 <= dados['média'] < 6:
    dados['situação'] = 'Recuperação'
elif 6 <= dados['média'] <= 10:
    dados['situação'] = 'Aprovado'
else:
    print('A média digitada está incorreta!')
print('-=' * 30)
for k, v in dados.items():
    print(f'- {k} é igual a {v}.')
