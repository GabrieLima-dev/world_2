# Escreva um progama que leia dois números inteiros e compare-os.
# mostrando na tela uma mensagem.

n1 = float(input('primero número: '))
n2 = float(input('segundo número: '))

if n1 > n2:
    print('O {} é maior que o {}.'.format(n1, n2))
if n1 < n2:
    print('O {} é maior que o {}.'.format(n2, n1))
if n1 == n2:
    print('Ambos são iguais.')