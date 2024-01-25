n = int(input('qual a ordem da matriz?:'))

mat =[[0 for x in range (n)]for x in range(n)]

for i in range(0,n):
    for j in range(0,n):
        mat[i][j] = int(input(f'elemento[{i},{j}]:'))

print()
print('diagonal principal:')
for i in range(0,n):
    print(mat[i][i],end=' ')

cont = 0

for i in range(0,n):
    for j in range(0,n):
        if mat[i][j] < 0 :
            cont = cont + 1

print()
print(f'quantidade de negativos = {cont}')
