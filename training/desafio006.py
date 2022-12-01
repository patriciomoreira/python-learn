#6.Digite um número inteiro, mostre o dobro, triplo e raiz quadrada.

num = int(input('Digite um número inteiro: '))

print('O número digitado foi {}, seu dobro é {}, triplo é {}, raiz quadrada é {:.0f}.'.format(
    num, num * 2, num * 3, num ** (1/2)))
