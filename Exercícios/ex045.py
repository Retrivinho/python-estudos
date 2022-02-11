from random import choice
escolhas = ['pedra', 'papel', 'tesoura']
cpu = choice(escolhas)
player = input('Pedra, Papel ou Tesoura?'
               '\n >> ').strip().lower()
if player not in escolhas:
    print('Não tente me passar para trás! Tchau.')
else:
    if (cpu == 'pedra' and player == 'tesoura')\
            or (cpu == 'tesoura' and player == 'papel')\
            or (cpu == 'papel' and player == 'pedra'):
        print(f'Hahaha, Perdeu! Joguei {cpu.capitalize()}.')
    elif cpu == player:
        print(f'Haha, empatou! Também joguei {cpu.capitalize()}')
    else:
        print(f'Aff, ganhou! Joguei {cpu.capitalize()}.')
