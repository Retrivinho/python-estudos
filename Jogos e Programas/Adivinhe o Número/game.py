import emoji
import pygame
import unidecode
from random import randint


def game(num, player):
    if num != player:
        sfx = pygame.mixer.Sound('erro.wav')
        pygame.mixer.Sound.play(sfx)
        print(emoji.emojize('Hahaha :joy:! Errou :sob:! Eu pensei no Nº{}'.format(num), use_aliases=True))
    else:
        sfx = pygame.mixer.Sound('acertou.wav')
        pygame.mixer.Sound.play(sfx)
        print(emoji.emojize('Não acredito :scream:! Acertou :tada:!!', use_aliases=True))


print("Você consegue acertar qual número estou pensando?")

while True:
    pygame.init()
    num_game = int(randint(1, 5))
    num_player = input("\nInsira um número de 1 a 5 e tente a sorte: ").strip()
    if not num_player.isnumeric():
        print('\n\nVocê está de sacanagem?')
    else:
        num_player = int(num_player)
        if num_player > 5:
            print('\nLEIA O ENUNCIADO DE NOVO: ')
        else:
            game(num_game, num_player)
            restart = str(input('\n\nDeseja jogar novamente?'
                                '\nSe não quiser, é só digitar Não.'
                                '\nCaso contrário, digite Continuar: ')).strip()
            if unidecode.unidecode(restart.lower()) == 'nao' or unidecode.unidecode(restart.lower()) == 'n':
                print('\nMeus parabéns, arregou!')
                break
