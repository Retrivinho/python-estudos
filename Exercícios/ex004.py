# Exemplos de uso de funções do Python

var = input('Digite algo: ')
print('Este valor é do tipo {}'.format(type(var)))
print('Este valor possui apenas espaços? {}'.format(var.isspace()))
print('Este valor é numérico? {}'.format(var.isnumeric()))
print('Este valor é alfabético? {}'.format(var.isalpha()))
print('Este valor é alfanumérico? {}'.format(var.isalnum()))
print('Este valor está em caixa alta? {}'.format(var.isupper()))
print('Este valor está em caixa baixa? {}'.format(var.islower()))
print('Este valor é capitalizado? {}'.format(var.istitle()))
