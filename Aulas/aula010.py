nome = str(input('Qual seu nome? '))
#print('Seu carro é novo' if tempo <= 3 else 'Seu carro é velho!')
if nome.count('Luis') > 0:
    print('Seu nome se parece com o meu!')
else:
    print('Seu nome não se parece com o meu...')
print('Bom dia, {}'.format(nome))
