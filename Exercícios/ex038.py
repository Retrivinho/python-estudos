n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
if n1 > n2:
    print('O primeiro número é maior que o segundo!')
elif n2 > n1:
    print('O segundo número é maior que o primeiro!')
elif n2 == n1:
    print('Os dois números são iguais!')
else:
    print('Não sei te informar!')
