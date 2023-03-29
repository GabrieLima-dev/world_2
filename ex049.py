# Refarça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando o laço for.
print(("-")*60)
print("Olá, seja bem vindo(a) a tabuada.")
number = int(input("Digite aqui um valor para calcularmos a sua tabuada."))
for c in range(1, 11):
    print("{} x {:2} = {}".format(number, c, number * c))
