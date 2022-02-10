l1 = lmenor1 = lmenor2 = lmaior = float(input('Primeiro lado: '))
l2 = float(input('Segundo lado: '))
if l2 < lmenor1:
    lmenor2 = l2
else:
    lmaior = l2
l3 = float(input('Terceiro lado: '))
if not l3 > lmenor1:
    lmenor2 = l3
if (lmenor1 + lmenor2) > lmaior:
    print('A soma dos lados menores é {}, e o lado maior é {}, portanto,'
          ' é possível formar um triângulo!'.format((lmenor1 + lmenor2), lmaior))
else:
    print('A soma dos lados menores é {}, e o lado maior é {}, portanto,'
          ' não é possível formar um triângulo!'.format((lmenor1 + lmenor2), lmaior))
