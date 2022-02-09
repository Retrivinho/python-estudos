from math import ceil
n1 = float(input('Digite a primeira nota: '))
if n1 > 10:
    print('Impossível!\nTente novamente!')
    exit()
n2 = float(input('Digite a segunda nota: '))
if n2 > 10:
    print('Impossível!\nTente novamente!')
    exit()
m = (n1 + n2) / 2
print('Sua média foi {:.1f}'.format(m))

if m >= 9.5:
    print('Espetacular, vou até arredondar para {}!'.format(ceil(m)))
elif m >= 6:
    print('Parabéns, você foi aprovado!')
elif 6 > m >= 5:
    print('Você foi aprovado, mas... Por pouco!')
else:
    print('Sinto muito, mas você não foi aprovado...')
