num = int(input('Digite o número que deseja saber a tabuada: '))
for c in range(1, 11):
    m = num * c
    print(f'{num} X {c} = {m}')
print(f'Essa é a tabuada do {num}.')
