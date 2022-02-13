soma = 0
for c in range(0, 500):
    if c % 3 == 0 and c % 2 != 0:
        soma += c
print(f'A soma de todos os números multiplos de 3 entre 0 e 500 é {soma} !')

