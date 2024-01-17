x = int(input('digite um numero:'))
y = int(input('digite outro numero:'))

if y < x :
    troca = x
    x = y
    y = troca

soma = 0

for c in range(x+1,y):
    if c % 2 != 0:
        soma = soma + c
    
print(f'soma dos impares = {soma}')