n1 = float(input('\nDigite a primeira nota: '))
n2 = float(input('\nDigite a segunda nota: '))
media = (n1 + n2) / 2
if media >= 7:
    print('\nParabéns!! Você foi aprovado! Sua média foi {}'.format(media))
elif 6.9 > media >= 5:
    print('\nRecuperação! Sua média foi {}. Se esforce mais.'.format(media))
elif media < 5:
    print('\nSinto lhe informar que você foi reprovado! Sua média foi {}. Que pena!'.format(media))
