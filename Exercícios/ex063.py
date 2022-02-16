n = int(input('Digite até qual dígito você deseja'
              '\na Seqência de Fibonacci: '))
sf = c = 0
anterior = 0
atual = 1
meio = 0
print(0)
while c < n - 1:
    meio = atual + anterior
    print(atual)
    anterior = atual
    atual = meio
    c += 1
