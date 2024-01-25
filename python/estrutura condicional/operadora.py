minutos = int(input('quantos minutos foram consumidos:'))

if minutos <= 100:
    print('valor a pagar = R$50.00')
else:
    tempo = minutos - 100
    multa = tempo * 2 + 50
    print(f'valor a pagar = R${multa:.2f}')
