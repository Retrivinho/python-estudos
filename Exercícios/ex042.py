l1 = lmenor1 = lmenor2 = lmaior = float(input('Primeiro lado: '))
l2 = float(input('Segundo lado: '))
if l2 < lmenor1:
    lmenor1 = l2
else:
    lmaior = l2
l3 = float(input('Terceiro lado: '))
if l3 > lmaior:
    lmenor2 = l2
    lmaior = l3
elif lmenor2 < l3 < lmaior or lmenor1 < l3 < lmaior:
    lmenor2 = l3
print(lmenor1, lmenor2, lmaior)
if (lmenor1 + lmenor2) > lmaior:
    if l1 == l2 == l3:
        tipo = 'Equilátero'
    elif l1 == l2 or l1 == l3 or l2 == l3:
        tipo = 'Isósceles'
    else:
        tipo = 'Escaleno'
    print('A soma dos lados menores é {}, e o lado maior é {}, portanto,'
          ' é possível formar um triângulo {}!'.format((lmenor1 + lmenor2), lmaior, tipo))
else:
    print('A soma dos lados menores é {}, e o lado maior é {}, portanto,'
          ' não é possível formar um triângulo!'.format((lmenor1 + lmenor2), lmaior))
