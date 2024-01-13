a = float(input('medida A:'))
b = float(input('medida B:'))
c = float(input('medida C:'))

quadrado = a ** 2 
triangulo = (a * b) / 2
trapezio = (a + b) * c / 2
print('-'*30)
print(f'area do quadrado:{quadrado:.4f}')
print(f'area do triangulo:{triangulo:.4f}')
print(f'area do trapézio:{trapezio:.4f}')
print('-'*30)
