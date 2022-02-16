n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite a razão: '))
c = soma = 0
while True:
    for c in range(n1, (n2 * 11), 10):
        soma += c
    break
print(f'A progressão aritmética dos 10 primeiros números\n'
      f'de {n1} com razão {n2} é {soma} !')
