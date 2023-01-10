# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal, não pode exceder 30% do salário ou então o empréstimo será negado.

price_home = float(input('Valor do imóvel: R$ '))
wage = float(input('Salário do comprador: R$ '))
year = int(input('Quantos anos de financiamento? '))
provision = price_home / (year * 12)
count = price_home * 0.3

print('Para pagar um imóvel de R${:.2f} em {} anos, a prestação será de R${:.2f}.'.format(
    price_home, year, provision))
if wage <= count:
    print('Empréstimo concedido!')
else:
    print('Empréstimo negado.')
