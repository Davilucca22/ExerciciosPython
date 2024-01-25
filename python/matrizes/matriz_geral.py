n = int(input('qual a ordem da matriz?:'))

mat = [[0 for x in range(n)]for x in range(n)]

for i in range(0,n):
    for j in range(0,n):
        mat[i][j] = int(input(f'elemento[{i},{j}]:'))

soma = 0

for i in range(0,n):
    for j in range(0,n):
        if mat[i][j] > 0:
            soma = soma + mat[i][j]

print('-'*30)
print(f'soma dos positivos:{soma}')
print('-'*30)

linha = int(input('escolha uma linha:'))

for i in range(0,n):
    for j in range(0,n):
        if linha == i :
            print(mat[i][j],end=' ')
print()
print('-'*30)

coluna = int(input('escolha uma coluna:'))

for i in range(0,n):
    for j in range(0,n):
        if coluna == j:
            print(mat[i][j],end=' ')
print()
print('-'*30)

print('diagonal principal:',end=' ')
for i in range(0,n):
    for j in range(0,n):
        if i == j:
            print(mat[i][j],end=' ')
print()
print('-'*30)
    
for i in range(0,n):
    for j in range(0,n):
        if mat[i][j] < 0:
            print(mat[i][j]**2,end=' ')
        else:
            print(mat[i][j],end=' ')
    print()
print('-'*30)
