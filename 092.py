from datetime import date
trabalho = dict()
trabalho['Nome'] = str(input('Nome: ')).strip().title()
ano = int(input('Ano do nascimento: '))
idade = date.today().year - ano
trabalho['Idade'] = idade
trabalho['ctps'] = int(input('Caretira de trabalho (0 não tem): '))
if trabalho['ctps'] != 0:
    trabalho['Contratação'] = int(input('Ano de contratação: '))
    trabalho['Salário'] = float(input('Salário: R$ '))
    trabalho['Aposentadoria'] = trabalho['Contratação'] - ano + 35
print('-=' * 30)
for k, v in trabalho.items():
    print(f'  - {k} tem valor {v}.')
