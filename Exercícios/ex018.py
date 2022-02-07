import math
angulo = math.radians(float(input('Digite o ângulo: ')))
sen = math.sin(angulo)
cos = math.cos(angulo)
tan = math.tan(angulo)
print('O seno de {}º é {}, o cosseno é {} e a tangente é {}'.format(math.degrees(angulo), sen, cos, tan))
