n = int(input('quantos numeros voce vai digitar?:'))

vet = [0 for x in range(n)]

for c in range(0,n):
    vet[c] = int(input('digite um numero:'))

maior = vet[0]
pos = 0

for c in range(0,n):
    if vet[c] > maior :
        maior = vet[c]
        pos = c

print(f'maior numero:{maior}')
print(f'posiçao do maior numero:{pos}')
