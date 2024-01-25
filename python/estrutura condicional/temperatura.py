esc = str(input('selecione a medida de temperatura\n[c] para celsius\n[f] para fahrenheit\nentrada:').lower())
if esc == 'f':
    print('-'*30)
    temp = float(input('digite a temperatura em fahrenheit:'))
    c = 5/9 * (temp - 32)
    print('-'*30)
    print(f'temperatura em celsius:{c:.2f} graus')
    print('-'*30)
elif esc == 'c':
    temp = float(input('digite a temperatura em graus celsius:'))
    f = temp * 9/5 + 32
    print('-'*30)
    print(f'temperatura em fahrenheit:{f:.2f} graus')
    print('-'*30)
else:
    print('valor invalido!')
    