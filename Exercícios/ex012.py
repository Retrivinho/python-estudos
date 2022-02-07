valor = float(input('Digite o valor do produto: R$'))
desconto = float(input('Digita o desconto em %: '))
valor_desconto = valor * (desconto / 100)
valor_total = valor - valor_desconto
print('O valor ficou em R$ {}!'.format(valor_total))
