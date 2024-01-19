n = int(input('quantos elementos terá o vetor?:'))
vet = [0 for x in range(0,n)]

for c in range(0,n):
    vet[c] = int(input('digite um numero:'))

soma = 0
cont = 0

for c in range(0,n):
    if vet[c] % 2 == 0:
        cont = cont + 1
        soma = soma + vet[c]

print('-'*30)
if cont > 1:
    media = soma / cont
    print(f'media dos numeros pares: {media:.1f}')
else:
    print('nenhum numero par digitado!')
print('-'*30)
