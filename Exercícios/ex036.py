casa = float(input('Digite o valor da casa: R$'))
salario = float(input('Digite o valor do seu salário: R$'))
parcelas = int(input('Em quantos anos você pretende pagar: ')) * 12
valor_parcela = casa / parcelas
max_parcela = salario * 0.30
if valor_parcela > max_parcela:
    print(f'\nEmpréstimo não liberado. Valor da parcela é de R$ {valor_parcela:.2f} '
          f'ultrapassa o valor máximo de R${max_parcela:.2f}.')
elif max_parcela == valor_parcela:
    print(f'\nEmpréstimo liberado! Serão {parcelas} parcelas de R${valor_parcela:.2f}!'
          '\nO valor da parcela equivale à 30% do seu salário! '
          '\nCuidado com as parcelas.')
else:
    print('\nParabéns! Seu empréstimo foi liberado. '
          f'\nSerão {parcelas} parcelas de R${valor_parcela:.2f}!'
          '\nSe atente ao vencimento das parcelas!')
