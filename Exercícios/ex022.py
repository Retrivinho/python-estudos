nome_completo = str(input('Nome completo: ')).strip()

# nsp_nome = ''.join(nome_completo.split()) AVANÇADO

print(nome_completo.upper())
print(nome_completo.lower())
print("Seu nome completo possui {} letras".format(len(nome_completo) - nome_completo.count(' ')))

# print("Seu primeiro nome possui {} letras".format(nome_completo.find(' ')))

nomes = nome_completo.split()
print("Seu primeiro nome possui {} letras".format(len(nomes[0])))
