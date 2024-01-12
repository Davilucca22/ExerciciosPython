print('digite dois numeros:')
n1 = int(input())
n2 = int(input())


soma = 0
if n1 > n2 :
    troca = n1
    n1 = n2
    n2 = troca

for c in range (n1+1,n2):
    if c % 2 != 0:
        soma = soma + c

print(f'soma dos impares:{soma}')
