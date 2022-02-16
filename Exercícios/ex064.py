soma = c = n = 0
while n != 999:
    n = int(input('Digite um número (para parar, digite 999): '))
    c += 1
    if n != 999:
        soma += n
print(f'Você digitou {c} números que somam {soma}')
