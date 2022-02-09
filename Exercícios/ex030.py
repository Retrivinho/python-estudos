num = input('Digite um número:').strip()
div = float(num) / 2
if not float.is_integer(div):
    print('Este número é impar!')
else:
    print('Este número é par!')
