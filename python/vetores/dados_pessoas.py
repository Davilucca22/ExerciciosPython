n = int(input('quantas pessoas serao digitadas?:'))

altura = [0 for x in range(n)]
genero = [0 for x in range(n)]

for c in range(0,n):
    altura[c] = float(input(f'altura da {c+1}º pessoa:'))
    genero[c] = str(input(f'genero da {c+1}º pessoa:').upper())

menor = altura[0]
maior = altura[0]

for c in range(0,n):
    if altura[c] > maior:
        maior = altura[c]

for c in range(0,n):
    if altura[c] < menor:
        menor = altura[c]

soma = 0
mulheres = 0

for c in range(0,n):
    if genero[c] == 'F':
        soma = soma + altura[c]
        mulheres = mulheres + 1

media = soma / mulheres

homens = 0

for c in range(0,n):
    if genero[c] == 'M':
        homens = homens + 1

print('-'*30)
print(f'maior altura : {maior}')
print(f'menor altura : {menor}')
print(f'media das alturas das mulheres:{media:.2f}')
print(f'quantidade de homens:{homens}')
print('-'*30)
