preco = float(input('Digite o valor da compra: R$ '))
print('Formas de pagamento:'
      '\n  1 - Dinheiro/Cheque'
      '\n  2 - Débito'
      '\n  3 - Crédito')
forma_pagamento = int(input('Digite a opção: '))
if forma_pagamento == 1:
    total = preco - (preco * 0.10)
    print(f'\nValor total com desconto de 10% é de R$ {total:.2f}')
elif forma_pagamento == 2:
    total = preco - (preco * 0.05)
    print(f'\nValor total com desconto de 5% é de R$ {total:.2f}')
elif forma_pagamento == 3:
    total = preco
    parcelas = int(input('Insira a quantidade de parcelas: '))
    if parcelas < 1:
        print('\nQuantidade de parcelas inválida! Volte do começo.')
    elif parcelas == 1:
        print(f'\nO valor total é de R$ {total:.2f}')
    else:
        if parcelas >= 3:
            total = preco + (preco * 0.20)
        print(f'\nO valor total com 20% de juros é de R$ {total:.2f}'
              f'\nem {parcelas} parcelas de R$ {total / parcelas:.2f}')
