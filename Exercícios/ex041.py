from datetime import date
atual = date.today().year
nasc = int(input('Digite o ano de nascimento: '))
if nasc >= atual or nasc < 1922:
    print("Não pode competir!")
    exit()
idade = atual - nasc
if idade < 9:
    print(f'Com {idade} anos, categoria MIRIM')
elif 14 > idade >= 9:
    print(f'Com {idade} anos, categoria INFANTIL')
elif 18 > idade >= 14:
    print(f'Com {idade} anos, categoria JUNIOR')
elif 21 > idade >= 18:
    print(f'Com {idade} anos, categoria SÊNIOR')
else:
    print(f'Com {idade} anos, categoria MASTER')
