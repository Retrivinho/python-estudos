heigth = float(input('Digite a altura da parede em metros: '))
width = float(input('Digita a largura da parede em metros: '))
metros_quadrados = heigth * width
litros_tinta = metros_quadrados / 2
print('Você precisará de {} litros de tinta para pintar {}m² de parede'.format(litros_tinta, metros_quadrados))
