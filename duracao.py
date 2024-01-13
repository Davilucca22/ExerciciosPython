tempo = int(input('digite um tempo em segundos:'))

hora = tempo // 3600
resto = tempo % 3600
minutos = resto // 60
segundos = resto % 60

print(f'{hora}:{minutos}:{segundos}')

