# Crie um programa que leia duas notas de um alçuno e calcule sua média,
# mostrando uma mensagem no final de acordo com a média atingida.
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
aver = (n1 + n2) / 2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}.'.format(
    n1, n2, aver))

if aver >= 7:
    print('O aluno está aprovado!')
elif 5 <= aver <= 6.9:
    print('O aluno está de recuperação!')
else:
    print('O aluno está reprovado!')
