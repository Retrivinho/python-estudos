peso = float(input('Digite o peso da 1ª pessoa: '))
pesado = leve = peso
for c in range(2, 6):
    peso = float(input(f'Digite o peso da {c}ª pessoa: '))
    if peso > pesado:
        pesado = peso
    elif peso < leve:
        leve = peso
    else:
        continue
print(f'A mais pesada pesa {pesado} Kg e a mais leva pesa {leve} Kg')
