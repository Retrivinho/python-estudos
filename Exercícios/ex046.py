from time import sleep
import datetime
print('O ano novo começa em...')
for c in range(10, 0, -1):
    print(c)
    sleep(1)
year = datetime.date.today().year
print(f'Feliz {year + 1}')
