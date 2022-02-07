dinheiro = float(input('Quantos R$ você tem na carteira? '))
dolar = input('Agora digite o valor do dolar atual. (Se pular essa etapa, será considerado o valor de 3.27): ')
if dolar == '':
    dolar = 3.27
money = dinheiro / float(dolar)
print('Então você possui U$ {:.2f} para gastar no Aliexpress!'.format(money))
