# A federação Nacional de Natação precisa de um programa
# que leia o ano de nascimento de um atreta e mostre a sua categoria.
from datetime import date
birth = int(input('Ano de nascimento: '))
year = date.today().year
age = year - birth
print('O atleta tem {} anos.'.format(age))
if age <= 9:
    print('Classificação: MIRIM')
if 10 <= age <= 14:
    print('Classificação: INFANTIL')
if 15 <= age <= 19:
    print('Classificação: JUNIOR')
if 20 <= age <= 25:
    print('Classificação: SÊNIOR')
if age > 25:
    print('Classificação: MASTER')
