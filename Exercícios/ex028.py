from random import randint
import emoji
num = int(randint(1, 5))
player = int(input("""Você consegue acertar qual número estou pensando?
Insira um número de 1 a 5 e tente a sorte: """))
if num == player:
    print(emoji.emojize('Não acredito :scream:! Acertou :tada:!!', use_aliases=True))
else:
    print(emoji.emojize('Hahaha :joy:! Errou :sob:! Eu pensei no Nº{}'.format(num), use_aliases=True))
