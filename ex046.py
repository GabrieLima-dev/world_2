# Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artificio, indo de 10 ate 0, com uma pausa de 1 segundo entre eles.
from time import sleep
for n in range(10, -1, -1):
    print(n)
    sleep(1)
print("FOGOOOS")
