salario = float(input('Insira o valor do seu salário: R$'))
aumento = float(input('Agora insira o aumento em %: '))
valor_aumento = salario * (aumento / 100)
salario_novo = salario + valor_aumento
print('Seu novo salário será de {} com {}% de aumento comparado ao anterior.'.format(salario_novo, aumento))
