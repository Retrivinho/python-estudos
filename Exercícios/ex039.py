from datetime import date
nasc = int(input('Digite o ano em que você nasceu: '))
atual = date.today().year
idade = atual - nasc
diff = (idade - 18)
if diff * -1 > 18:
    print('Ainda falta muito tempo para você se alistar!')
elif idade > 18:
    print('Já passou da hora de se alistar!'
          f'\nDeveria ter se alistado a {diff} ano(s) atrás!')
elif idade < 18:
    print('Você ainda irá se alistar! '
          f'\nFaltam {diff * -1} ano(s)!')
elif idade == 18:
    print('Esse ano você deverá se alistar!')

