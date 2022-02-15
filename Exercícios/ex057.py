while True:
    s = str(input('Qual seu sexo? [F/M] \n >>')).lower()
    if s == 'f':
        print('Feminino')
        break
    elif s == 'm':
        print('Masculino')
        break
    else:
        continue
