# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o.
sum = 0
for number in range(1, 7):
    num = int(input("Digite o {}° valor: ".format(number)))
    if number % 2 == 0:
        sum = sum + number
print("A soma dos números pares foi igual a {}.".format(sum))