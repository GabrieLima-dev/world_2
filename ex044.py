# Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# – à vista dinheiro/cheque: 10% de desconto
# – à vista no cartão: 5% de desconto
# – em até 2x no cartão: preço formal
# – 3x ou mais no cartão: 20% de juros

print('='*10 + ' LOJAO DOS ELETROS ' + '='*10)
price = float(input('Preço das compras: R$ '))

print(''' 
--------FORMAS DE PAGAMENTO--------
[ 1 ] À VISTA DINHEIRO/PIX/CHEQUE
[ 2 ] À VISTA CARTÃO/DÉBITO
[ 3 ] 2X NO CARTÃO/CRÉDITO
[ 4 ] 3X OU MAIS NO CARTÃO/CRÉDITO ''')

option = int(input('''
Qual a opção? '''))

if option == 1:
    finish = price - (price * 0.10)
elif option == 2:
    finish = price - (price * 0.05)
elif option == 3:
    finish = price
elif option == 4:
    portion = int(input('Quantas parcelas: '))
    count = (price / portion)
    fees = count + (count * 0.20)
    print('''
Sua compra será parcelada em {}x de R${:.2f} com juros.'''.format(portion, fees))
    finish = portion * fees
else:
    finish = price
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente.')

print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(
    price, finish))
