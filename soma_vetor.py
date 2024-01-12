n = int(input('quantos elementos voce vai digitar:'))
vetor = [0 for x in range(n)]

for c in range(0,n):
    vetor[c] = int(input('digite um numero:'))

print('valores = ',end='')
for c in range (0,n):
    print(f'{vetor[c]} ',end='')

soma = 0 
for c in range(0,n):
    soma = soma + vetor[c]
print()
print(f'soma = {soma}')

media = soma / n
print(f'media = {media}')
