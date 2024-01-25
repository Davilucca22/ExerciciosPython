larg = float(input('largura do terreno:'))
comp = float(input('comprimento do terreno:'))
valorMetro = float(input('valor do metro quadrado:'))

area = larg * comp
valorTerreno = area * valorMetro
print('-' * 30)
print(f'area do terreno:{area} m²')
print(f'preço do terreno:R${valorTerreno}')
print('-'* 30)