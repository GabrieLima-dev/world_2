# Crie um programa que faça o computador jogar Jokenpô com você.
import time
import random
print('='*10 + ' JOKENPÔ ' + '='*10)
print('''
Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA
''')

move = int(input('Qual a sua jogada? '))
print('JO')
time.sleep(0.5)
print('KEN')
time.sleep(0.5)
print('PÔ!!!')
itens = ('pedra', 'papel', 'tesoura')
pc = random.randint(0, 2)

if move == 0:
    if pc == 0:
        result = 'empata'
    elif pc == 1:
        result = 'perde'
    elif pc == 2:
        result = 'ganha'
elif move == 1:
    if pc == 0:
        result = 'ganha'
    elif pc == 1:
        result = 'empata'
    elif pc == 2:
        result = 'perde'
elif move == 2:
    if pc == 0:
        result = 'perde'
    elif pc == 1:
        result = 'ganha'
    elif pc == 2:
        result = 'empata'

print('-='*15)
print('''
Computador jogou {}
Jogador jogou {}
'''.format(itens[pc], itens[move]))
print('-='*15)

print(''' 
O jogador {}'''.format(result))
