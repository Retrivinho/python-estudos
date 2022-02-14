nome = str(input('Digite o nome da 1ª pessoa: '))
velho = idade = int(input('Agora a idade: '))
sexo  = str(input('Agora o sexo: ')).strip().lower()
mais_velho = 'Ninguém'
menores_20 = 0
idade_total = 0
for c in range(2, 5):
    nome  = str(input(f'Digite o nome da {c}ª pessoa: '))
    idade = int(input('Agora a idade: '))
    idade_total += idade
    sexo  = str(input('Agora o sexo: ')).strip().lower()
    if sexo == 'masculino' and idade > velho:
        mais_velho = nome
    if sexo == 'feminino' and idade < 20:
        menores_20 += 1
print(f'A média de idade deste grupo é {idade / 4}')
print(f'O nome do homem mais velho é {mais_velho}')
print(f'A quantidade de mulheres menores de 20 anos é de {menores_20}')
