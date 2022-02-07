frase = str(input('Digite uma frase: ')).lower().strip()
print('Sua frase possui {} vez(es) a letra A!'.format(frase.count('a')))
print('A posição que a letra A aparece pela primeira vez é {}'.format(frase.find('a')+1))
print('A posição que a letra A aparece pela última vez é {}'.format(frase.rfind('a')+1))
