from math import sqrt, pow
cateto_oposto = float(input('Insira o comprimento do Cateto Oposto: '))
cateto_adjacente = float(input('Insira o comprimento do Cateto Adjacente: '))
hipotenusa = pow(cateto_oposto, 2) + pow(cateto_adjacente, 2)
print('O valor da hipotenusa é {}'.format(sqrt(hipotenusa)))
