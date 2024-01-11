import math
base = float(input('digite a base do reatangulo:'))
altura = float(input('digite a altura do retangulo: '))
area = base * altura
perimetro = (2*base) + (2*altura)
diagonal = math.exp(base**2 + altura**2)
print(f'area do retangulo:{area}')
print(f'perimetro do retangulo:{perimetro}')
print(f'diagonal do retangulo:{diagonal:.2f}')
