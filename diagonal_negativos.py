n = int(input('qual a ordem da matriz?:'))
mat = [[0 for x in range (n)] for x in range(n)]
for i in range (0,n):
    for j in range (0,n):
        mat[i][j] = int(input(f'elemento[{i},{j}]:'))

print('diagonal principal:',end='')
for i in range (0,n):
    print(f'{mat[i][i]} ',end='')
print()

cont = 0 
print('qunatidade de negativos = ',end='')
for i in range(0,n):
    for j in range(0,n):
        if mat[i][j] < 0 :
            cont = cont + 1
print(cont)
