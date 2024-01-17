n1 = float(input('digite a primeira nota:'))

while n1 < 0 or n1 > 10:
    n1 = float(input('valor invalido!tente novamente:'))

n2 = float(input('digite a segunda nota:'))
while n2 < 0 or n2 > 10:
    n2 = float(input('valor invalido!tente novamente:'))

media = (n1 + n2) / 2

print('-'*30)
print(f'media:{media:.2f}')
print('-'*30)
