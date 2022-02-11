import sys
import time


def typrint(s, t=.005):
    for letter in s:
        sys.stdout.write(letter)
        time.sleep(t)


typrint('\nBem vindo ao nosso Sistema de Atendimento Automático!')
typrint('\n - Você pode digitar SAIR à qualquer momento para encerrar o serviço', 0.05)
typrint('\n - O comprovante do pagamento deverá ser apresentado na saída!', 0.05)
typrint('\nCadastre-se no nosso aplicativo para receber todas as ofertas!')
while True:
    while True:
        preco = input('\nValor da compra: R$ ').strip().lower()
        if preco == 'sair':
            typrint('Encerrando serviço...')
            exit()
        elif not preco.isnumeric():
            print('Digite o valor correto!')
            continue
        else:
            preco = float(preco)
            break
    while True:
        print('Formas de pagamento:'
              '\n  1 - Dinheiro/Cheque'
              '\n  2 - Débito'
              '\n  3 - Crédito')
        forma_pagamento = input('Digite a opção: ').strip()
        if forma_pagamento == 'sair':
            typrint('Encerrando serviço...')
            exit()
        if not forma_pagamento.isnumeric() or int(forma_pagamento) > 3:
            print('Forma de pagamento inválida!')
            continue
        else:
            forma_pagamento = int(forma_pagamento)
            break
    if forma_pagamento == 1:
        total = preco - (preco * 0.10)
        typrint(f'\nValor total com desconto de 10% é de R$ {total:.2f}')
    elif forma_pagamento == 2:
        total = preco - (preco * 0.05)
        typrint(f'\nValor total com desconto de 5% é de R$ {total:.2f}')
    elif forma_pagamento == 3:
        total = preco
        while True:
            parcelas = input('Insira a quantidade de parcelas: ').strip()
            if parcelas == 'sair':
                typrint('Encerrando serviço...')
                exit()
            if not parcelas.isnumeric() or int(parcelas) < 1:
                print('Quantidade de parcelas incorreta!')
                continue
            else:
                parcelas = int(parcelas)
                break
        if parcelas < 1:
            typrint('\nQuantidade de parcelas inválida! Volte do começo.')
        elif parcelas == 1:
            typrint(f'\nO valor total é de R$ {total:.2f}')
        else:
            if parcelas >= 3:
                total = preco + (preco * 0.20)
            typrint(f'\nO valor total com 20% de juros é de R$ {total:.2f}'
                    f'\nem {parcelas} parcelas de R$ {total / parcelas:.2f}')
    typrint('\n\nRETIRE SEU CUPOM AO LADO PARA APRESENTAR NA SAÍDA!!', 0.05)
    typrint('\n\nObrigado por comprar com a gente!')
    typrint('\nAgradecemos sua visita.')
    break
