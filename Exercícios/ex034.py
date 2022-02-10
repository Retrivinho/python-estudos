salario = float(input('Qual seu salário? R$ '))
if salario > 1250:
    salario = salario + (salario * 0.10)
    print('Seu novo salário com 10% de aumento será de R$ {}.'.format(salario))
else:
    salario = salario + (salario * 0.15)
    print('Seu novo salário com 15% de aumento será de R$ {}.'.format(salario))
