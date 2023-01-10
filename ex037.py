num = int(input('Digite um número inteiro: '))

print('''
Escolha uma das opções abaixo:
[ 1 ] Converter para Binário
[ 2 ] Converter para Octal
[ 3 ] Converte para Hexadecimal''')

option = int(input('Sua opção: '))

if option == 1:
    print('{} convertido para Binário é igual a {}'.format(num, bin(num)[2:]))
elif option == 2:
    print('{} convertido para Octal é igual a {}'.format(num, oct(num)[2:]))
elif option == 3:
    print('{} convertido para Hexadecimal é igual a {}'.format(num, hex(num)[2:]))
else:
    print('Você digitou uma opção inválida, tente novamente.')
