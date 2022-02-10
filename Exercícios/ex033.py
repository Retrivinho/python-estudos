menor = maior = int(input('Insira o primeiro número: '))
n2 = int(input('Insira o segundo número: '))
if n2 > maior:
    maior = n2
else:
    menor = n2
n3 = int(input('Insira o terceiro número:'))
if n3 > maior:
    maior = n3
elif n3 < menor:
    menor = n3
print('O maior número é {} e o menor é {}.'.format(maior, menor))
