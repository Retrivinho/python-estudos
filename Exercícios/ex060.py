n1 = int(input('Digite um número para saber seu fatorial: '))
f = 1
i = 2
while n1 >= i:
    f = f * i
    i = i + 1
print(f'O fatorial de {n1} é {f}!')
