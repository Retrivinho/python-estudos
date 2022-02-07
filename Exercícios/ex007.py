p1 = int(input('Digite a nota da primeira prova: '))
p2 = int(input('Digita a nota da segunda prova: '))
media = (p1 + p2) / 2
if media > 5:
    print('Sua média foi {}... Você foi aprovado!'.format(media))
elif 5 > media > 4:
    print('Passou raspando! Sua média foi {}'.format(media))
else:
    print('Sua média foi {} e você está reprovado!'.format(media))
