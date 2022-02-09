print('Bem vindo ao serviço de multas do DETRAN')

while True:
    vel = input('Digite a velocidade que o carro passou em Km/h: ')
    if not vel.isnumeric():
        print('Insira um valor numérico!')
    else:
        vel = float(vel)
        if vel <= 80:
            print('O carro não foi multado!')
            restart = input('Deseja continuar utilizando nosso serviço? (S/N): ')
            if restart.lower() == 'n':
                print('Obrigado por utilizar nossos serviços!')
                break
        else:
            multa = (vel - 80) * 7
            print('O valor da multa é de R$ 7.00 para cada KM excedente ao limite'
                  'Neste caso, o valor da multa é de R$ {:.2f}'.format(multa))
            restart = input('Deseja continuar utilizando nosso serviço? (S/N): ')
            if restart.lower() == 'n':
                print('Obrigado por utilizar nossos serviços!')
                break
