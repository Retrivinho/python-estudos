n1 = float(input('Digite o primeiro valor: '))
n2 = float(input('Digite o segundo valor: '))

while True:
    option = input('Escolha a operação:'
                   '\n  [1] Soma'
                   '\n  [2] Multiplicar'
                   '\n  [3] Maior'
                   '\n  [4] Novos números'
                   '\n  [5] Sair '
                   '\n>>')
    if not option.isnumeric():
        print('Opção inválida!')
        continue
    elif int(option) == 1:
        print(f'A soma de {n1} e {n2} é {n1 + n2}')
        break
    elif int(option) == 2:
        print(f'O produto de {n1} e {n2} é {n1 * n2}')
        break
    elif int(option) == 3:
        if n1 > n2:
            print(f'{n1} é maior que {n2}')
            break
        elif n2 > n1:
            print(f'{n2} é maior que {n1}')
            break
        else:
            print('Os valores são iguais!')
            break
    elif int(option) == 4:
        n1 = float(input('Digite o primeiro novo valor: '))
        n2 = float(input('Digite o segundo novo valor: '))
        continue
    elif int(option) == 5:
        print('Obrigado pela participação!')
        break

