import emoji
import pygame
import unidecode
from random import randint


def game(num, player):
    if num != player:
        sfx = pygame.mixer.Sound('erro.wav')
        pygame.mixer.Sound.play(sfx)
        print('\033[0:33:36m-=-\033[m' * 20)
        print(emoji.emojize('\033[7:31:32mHahaha :joy:! Errou :sob:! Eu pensei no Nº{}\033[m'.format(num),
                            use_aliases=True))
        print('\033[0:33:36m-=-\033[m' * 20)
    else:
        sfx = pygame.mixer.Sound('acertou.wav')
        pygame.mixer.Sound.play(sfx)
        print('\033[0:33:36m-=-\033[m' * 20)
        print(emoji.emojize('\033[0:32:40mNão acredito :scream:! Acertou :tada:!!\033[m', use_aliases=True))
        print('\033[0:33:36m-=-\033[m' * 20)


print("\033[7:32:40mVocê consegue acertar qual número estou pensando?\033[m")

while True:
    pygame.init()
    num_game = int(randint(1, 5))
    num_player = input("\033[0:32:40m   Insira um número de 1 a 5 e tente a sorte:    ").strip()
    if not num_player.isnumeric():
        print('\n\n\033[7:32:40mVocê está de sacanagem?\033[m')
    else:
        num_player = int(num_player)
        if num_player > 5:
            print('\n\033[0:32:40mLEIA O ENUNCIADO DE NOVO: \033[m')
        else:
            game(num_game, num_player)
            restart = str(input('\033[0:32:40mDeseja jogar novamente?\033[m'
                                '\n\033[7:32:40mSe não quiser, é só digitar Não.\033[m'
                                '\n\033[0:32:40mCaso contrário, aperte Enter: \033[m')).strip()
            if unidecode.unidecode(restart.lower()) == 'nao' or unidecode.unidecode(restart.lower()) == 'n':
                print('\n\033[7:32:40mMeus parabéns, arregou!\033[m')
                break
