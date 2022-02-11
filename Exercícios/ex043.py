altura = float(input('Insira a sua altura em Metros: '))
if altura > 3:
    print('A altura deve estar incorreta!')
    exit()
peso = float(input('Insira seu peso em Kg: '))
if peso > 450:
    print('Se este for seu peso real, está com obesidade morbida!')
    exit()
imc = peso / (altura ** 2)
print(f'Seu IMC é de {imc:.2f}.')
if imc <= 18.5:
    print('Você está abaixo do peso.')
elif 25 >= imc > 18.5:
    print('Você está no peso ideal!')
elif 30 >= imc > 25:
    print('Você está com sobrepeso.')
elif 40 >= imc > 30:
    print('Você está com obesidade.')
elif imc > 40:
    print('Você está como obesidade mórbida!')
