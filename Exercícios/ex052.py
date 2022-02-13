n = int(input('Digite um número: '))
resto = 0
for c in range(2, 11):
    resto += n % c
if resto != 0:
    print(f'{n} é primo!')
else:
    print(f'{n} não é primo!')
