km_viagem = float(input('Digite em Km a distância da viagem: '))
if km_viagem > 200:
    print('Você gastará R$0.45 por Km, totalizando R$ {} !'.format(km_viagem * 0.45))
else:
    print('Você gastará R$ 0.50 por Km, totalizando R$ {} !'.format(km_viagem * 0.50))
