n = int(input('quantos elementos o vetor terá?:'))

vet = [0 for x in range(n)]

soma = 0

for c in range(0,n):
    vet[c] = float(input('digite um numero:'))
    soma = soma + vet[c]

media = soma / n

print('-'*30)
print(f'media do vetor:{media:.3f}')
print('elementos abaixo da media:')
for c in range(0,n):
    if vet[c] < media:
        print(vet[c])
print('-'*30)
