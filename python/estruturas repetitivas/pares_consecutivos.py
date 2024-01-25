x = int(input('digite um numero inteiro:'))

if x % 2 == 1:
    x = x + 1

soma = x + (x+2) + (x+4) + (x+6) + (x+8)

print(f'soma = {soma}')