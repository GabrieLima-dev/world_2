print(('-=')*13)
print('Analisador de Triângulos')
print(('-=')*13)
a = int(input('Primeiro segmento: '))
b = int(input('Segundo segmento: '))
c = int(input('Terceiro segmento: '))

if a + b > c and b + c > a and a + c > b:
    print('''
    Os segmentos acima podem formar triângulo''', end=' ')
    if a == b == c:
        print('equilátero.')
    elif a != b != c != a:
        print('escaleno.')
    else:
        print('isósceles')
else:
    print('''
    Os segmentos acima não podem formar triângulo!''')
