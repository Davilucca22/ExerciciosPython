n = int(input('quantos numeros voce vai digitar?:'))

vet = [0 for x in range(n)]

soma = 0

for c in range (0,n):
    vet[c] = int (input('digite um numero:'))
    soma = soma + vet[c]

media = soma / n

print('-'*30)
print('valores:',end=' ')
for c in range(0,n): 
    print(vet[c],end=' ')

print()
print('-'*30)
print(f'soma dos valores:{soma}')
print('-'*30)
print(f'media dos valores:{media:.2f}')
print('-'*30)