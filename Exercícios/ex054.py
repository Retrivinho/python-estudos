maiores = 0
menores = 0
for c in range(1, 8):
    idade = int(input(f'Digite a idade da {c}º pessoa: '))
    if idade >= 18:
        maiores += 1
    else:
        menores += 1
print(f'São {maiores} pessoas maiores de idade e {menores} menores de idade.')
