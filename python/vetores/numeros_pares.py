n = int(input('quantos numeros voce vai digitar?:'))

vet = [0 for x in range(n)]

cont = 0

for c in range(0,n):
    vet[c] = int(input('digite um numero:'))
    if vet[c] % 2 == 0:
        cont = cont + 1

print('-'*30) 
print('numeros pares:',end=' ')
for c in range(0,n):
    if vet[c] % 2 == 0:
        print(vet[c],end=' ')
print()
print('-'*30)

print(f'quantidade de pares = {cont}')