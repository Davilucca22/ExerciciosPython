n = int(input('qual a ordem da matriz?:'))
mat = [[0 for x in range (n)]for x in range (n)]

for i in range(0,n):
    for j in range(0,n):
        mat[i][j] = int(input(f'elemento[{i},{j}]:'))

soma = 0

for i in range (0,n):
    for j in range(0,n):
        if j > i :
            soma = soma + mat[i][j]

print(f'soma dos elementos acima da diagonal principal = {soma}')
