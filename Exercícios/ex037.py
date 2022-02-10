num = input('Digite o número que deseja converter: ')
if not num.isnumeric():
    print('DIGITE UM NÚMERO!')
else:
    num = int(num)
base = input('Qual base você deseja converter?'
             '\n   1 - Binário'
             '\n   2 - Octal'
             '\n   3 - Hexadecimal'
             '\n Digite sua escolha: ')
if not base.isnumeric():
    print('Escolha uma base da lista!')
else:
    base = int(base)
if base == 1:
    num = bin(num)
    print(f'Seu número convertido para binário é {num} !')
elif base == 2:
    num = oct(num)
    print(f'Seu número convertido para octal é {num} !')
elif base == 3:
    num = hex(num)
    print(f'Seu número convertido para hexadecimal é {num} !')
else:
    print(f'Opção não existe na lista, tente novamente.')
