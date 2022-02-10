import unidecode

print('Bem vindo ao serviço de multas do DETRAN')


def multa(velocidade):
    velocidade = float(velocidade)
    if velocidade <= 80:
        print('O carro não foi multado!')
    else:
        valor_km = input('Valor da multa por Km/h: ')
        if not vel.isnumeric():
            print('Insira um valor numérico!')
        else:
            valor_km = float(valor_km)
            valor_multa = (velocidade - 80) * valor_km
            print('O valor da multa é de R$ {:.2f} para cada KM excedente ao limite'
                  'Neste caso, o valor da multa é de R$ {:.2f}'.format(valor_km, valor_multa))


while True:
    vel = input('Digite a velocidade que o carro passou em Km/h: ').strip()
    if not vel.isnumeric():
        print('Insira um valor numérico!')
    else:
        multa(vel)
        restart = unidecode.unidecode(str(input('Deseja continuar utilizando nosso serviço? (S/N): '))).strip().lower()
        if restart == 'nao' or restart == 'n':
            print('Obrigado por utilizar nossos serviços!')
            break
