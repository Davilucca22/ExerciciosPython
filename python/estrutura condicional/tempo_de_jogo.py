inicio = int(input('hora inicial do jogo:'))
fim = int(input('hora final do jogo:'))

if inicio >= fim :
    tempo = (24 - inicio) + fim
else:
    tempo = fim - inicio
print('-'* 30)
print(f'tempo de jogo:{tempo} horas')
print('-'* 30)