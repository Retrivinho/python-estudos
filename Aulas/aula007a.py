n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
soma = n1 + n2
sub = n1 - n2
multi = n1 * n2
div = n1 / n2
divi = n1 // n2
exp = n1 ** n2
rest = n1 % n2
print('A soma dos números é {},\n a subtração é {},\n a multiplicação é {}'.format(soma, sub, multi))
print('A divisão é {:.3f},\n a divisão inteira é {}'.format(div, divi))
print('Exponenciação é {}\n e o resto da divisão é {}'.format(exp, rest))
