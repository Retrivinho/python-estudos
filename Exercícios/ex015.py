dias       = int(input('Por quantos dias o carro foi alugado? '))
km_rodado  = float(input('Quantos Km foram rodados com o carro? '))
if dias == '':
  dias = 0
if km_rodado == '':
  km_rodado = 0
valor_dias = dias * 60
valor_km   = km_rodado * 0.15
print('O valor do aluguel por diária é R${} e \no valor por quilometragem é R${}'.format(valor_dias, valor_km))
print('Total: R$', valor_dias + valor_km)
