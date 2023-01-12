# Faça um programa que leia o ano de nascimento de um jovem e informe,
# de acordo com sua idade, se ele ainda vai se alistar ao serviço militar,
# se é a hora de se alistar, ou se passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date
birth = int(input('Ano de nascimento: '))  # ano de nascimento
current_year = date.today().year          # ano atual
year = current_year - birth               # quantos anos

print('Quem nasceu em {} tem {} anos em {}.'.format(birth, year, current_year))

if year < 18:
    print('Ainda faltam {} ano(s) para o alistamento.'.format(18 - year))
    print('Seu alistamento será em {}.'.format(current_year + (18 - year)))
elif year == 18:
    print('Você tem que se alistar imediatamente!')
else:
    print('Você já deveria ter se alistado há {} ano(s).'.format(year - 18))
    print('Seu alistamento foi em {}.'.format(current_year - (18 - year)))
