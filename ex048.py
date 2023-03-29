# Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 ate 500.
sum = 0
for odd in range(1, 501, 2):
    if odd % 3 == 0:
        sum = sum + odd
print("A soma de todos os valores são: {}".format(sum))