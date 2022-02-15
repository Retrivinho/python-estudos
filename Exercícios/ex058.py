from random import randint
num = int(randint(1, 10))
print("Você consegue acertar qual número estou pensando?")
tentativas = 1
while True:
    player = int(input("Insira um número de 1 a 10 e tente a sorte: "))
    if num == player:
        print(f'Não acredito! Acertou!! Pensei no número {num}')
        break
    else:
        print('Hahaha! Errou! Tenta de novo!'
              '\n>> ')
        tentativas += 1
        continue
if tentativas == 1:
    print('De primeira!')
else:
    print(f'Precisou de {tentativas} tentativas!')
