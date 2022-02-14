import unidecode

frase = str(input('Frase: ')).strip().lower()
frase = unidecode.unidecode(frase)
frase = frase.replace(' ', '')
if frase[::-1] == frase:
    print(frase[::-1])
    print('É palíndromo')
else:
    print(frase[::-1])
    print('Não é palíndromo')
