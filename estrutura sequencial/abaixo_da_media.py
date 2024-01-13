n = int(input('quantos elementos o vetor terá?:'))
vet = [0 for x in range (n)]

soma = 0

for i in range (0,n):
    vet[i] = int(input('digite um numero:'))
    soma = soma + vet[i]

media = soma / n

print(f'a media do vetor é de {media}')
print('numeros abaixo da media:')
for i in range (0,n):
    if vet[i] < media:
        print(vet[i])


