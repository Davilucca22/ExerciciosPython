from math import sqrt
a = float(input('coeficiente A:'))
b = float(input('coeficiente B:'))
c = float(input('coeficiente C:'))

delta = (b**2) - 4 * a * c

if delta < 0 or a == 0 :
    print('essa equaçao nao possui raizes reais!')
else:
    x1 = (-b + sqrt(delta) ) / (2 * a)
    x2 = (-b - sqrt(delta)) / (2 * a)
    print(f'X1 = {x1:.4f}')
    print(f'X2 = {x2:.4f}')