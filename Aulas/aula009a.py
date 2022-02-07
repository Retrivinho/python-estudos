cpf = str(input('Digite seu CPF: '))
cpf_formatado = cpf.replace('.', '').replace('-', '')
print('{}.{}.{}-{}'.format(cpf_formatado[0:3], cpf_formatado[3:6], cpf_formatado[6:9], cpf_formatado[9:11]))
