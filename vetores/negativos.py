n = int(input('quantos numeros voce vai digitar?:'))

vet = [0 for x in range(n)]

for c in range(0,n):
    vet[c] = int(input('digite um numero:'))
print('-'*30)
print('numeros negativos:')

for c in range(0,n):
    if vet[c] < 0 :
        print(vet[c])
print('-'*30)