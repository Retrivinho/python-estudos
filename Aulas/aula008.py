from math import sqrt, ceil
num = int(input('Digite um número: '))
raiz = ceil(sqrt(num))
print('A raiz de {} é {:.2f}'.format(num, float(raiz)))
