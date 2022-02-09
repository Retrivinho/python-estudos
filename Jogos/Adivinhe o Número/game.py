import emoji
from random import randint
from playsound import playsound

num = int(randint(1, 5))
player = int(input("""Você consegue acertar qual número estou pensando?
Insira um número de 1 a 5 e tente a sorte: """))

if num == player:
    playsound('acertou.mp3', True)
    print(emoji.emojize('Não acredito :scream:! Acertou :tada:!!', use_aliases=True))
else:
    playsound('erro.mp3', True)
    print(emoji.emojize('Hahaha :joy:! Errou :sob:! Eu pensei no Nº{}'.format(num), use_aliases=True))

