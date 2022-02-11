import sys
import time
import pygame
from random import choice


def typrint(s, t=.005):
    for letter in s:
        sys.stdout.write(letter)
        time.sleep(t)


pygame.init()

while True:
    escolhas = ['pedra', 'papel', 'tesoura']
    cpu = choice(escolhas)

    player = input('Pedra, Papel ou Tesoura?'
                   '\n >> ').strip().lower()
    if player not in escolhas:
        typrint('Não tente me passar para trás!\n')
        continue
    else:
        if (cpu == 'pedra' and player == 'tesoura') \
                or (cpu == 'tesoura' and player == 'papel') \
                or (cpu == 'papel' and player == 'pedra'):
            if cpu == 'pedra':
                sfx = pygame.mixer.Sound('olha_a_pedra.wav')
                pygame.mixer.Sound.play(sfx)
            else:
                sfx = pygame.mixer.Sound('perdeu.wav')
                pygame.mixer.Sound.play(sfx)
            typrint(f'Hahaha, Perdeu! Joguei {cpu.capitalize()}.')
        elif cpu == player:
            sfx = pygame.mixer.Sound('empatou.wav')
            pygame.mixer.Sound.play(sfx)
            typrint(f'Empatou! Também joguei {cpu.capitalize()}')
        else:
            sfx = pygame.mixer.Sound('ganhou.wav')
            pygame.mixer.Sound.play(sfx)
            typrint(f'Aff, ganhou! Joguei {cpu.capitalize()}.')
    restart = input('\nQuer jogar de novo? (S/N)\n>> ').strip().lower()
    if restart == 'n' or restart == 'nao':
        print('Até mais então...')
        break
    elif restart == 's' or restart == 'sim':
        print('Então vamos mais uma!')
        continue
    else:
        sfx_cpu = pygame.mixer.Sound('adeus.wav')
        pygame.mixer.Sound.play(sfx_cpu)
        print('KKKKKKKKKK TIO TÁ AI? TILTA NÃO, JA JA TEM MAIS.')
        time.sleep(4)
        break
