# Desenvolva um programa que leia o primeiro termo e a razão de um PA. Nofinal,  mostre os 10 primeiros termos dessa progressão.

first_term = int(input("Digite op primeiro termo: "))
rate = int(input("Digite agora a razão da PA: "))
tenth = first_term + (10 - 1) * rate
for number in range(first_term, tenth + 1, rate):
    print(" {} ".format(number), end=" -> ")
print(" ...")
