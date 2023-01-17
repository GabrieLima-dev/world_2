# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule o IMC e mostre seu status.
weight = int(input('Qual é o seu peso? (Kg) '))
height = float(input('Qual é a sua altura? (m) '))
imc = weight / (height * height)
print('O imc dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está abaixo do peso.')
elif 18.5 <= imc < 25:
    print('Você está no peso ideal.')
elif 25 <= imc < 30:
    print('Você está no sobrepeso.')
elif 30 <= imc < 40:
    print('Você está na obesidade.')
elif imc > 40:
    print('Você está na obesidade mórbida.')
