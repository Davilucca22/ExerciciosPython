print('-'*30)
print('digite as tres distancias atingidas pelos dardos')
print('-'*30)
d1 = float(input('1ª distancia:'))
d2 = float(input('2ª distancia:'))
d3 = float(input('3ª distancia:'))

maior = 0
if d1 > d2 and d1 > d3:
    maior = d1
elif d2 > d3 :
    maior = d2
else:
    maior = d3

print('-'*30)
print(f'maior distancia:{maior}m')
print('-'*30)
