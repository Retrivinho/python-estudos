def converter(base, num):
    base = int(base)
    num = int(num)
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
        print(' Opção inválida!')


tentativas = 0
while tentativas < 3:
    n1 = input('Digite o número que deseja converter: ')
    if not n1.isnumeric():
        print('DIGITE UM NÚMERO!')
        tentativas = tentativas + 1
    else:
        base_numerica = input('Qual base você deseja converter?'
                              '\n   1 - Binário'
                              '\n   2 - Octal'
                              '\n   3 - Hexadecimal'
                              '\n Digite sua escolha: ')
        if not base_numerica.isnumeric():
            print('Escolha uma base da lista!')
            tentativas = tentativas + 1
        converter(base_numerica, n1)
        restart = input('\nDeseja converter outro número? (S/N): ').strip().lower()
        if restart == 's':
            print('\nVamos continuar...\n')
            continue
        elif restart == 'n':
            print('\nObrigado por usar nosso sistema!')
            print('\nFique à vontade para utilizar novamente!')
            break
        else:
            print('\nOpção Inválida. Encerrando...')
            print('\n\nServiço encerrado!')
            break
else:
    print('Serviço encerrado!')
