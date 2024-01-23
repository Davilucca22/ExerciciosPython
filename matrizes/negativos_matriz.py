l = int(input('quantas linhas a matriz terá?:'))
c = int(input('quantas colunas a matriz terá?:'))

mat = [[0 for x in range(c)]for x in range(l)]

for i in range(0,l):
    for j in range(0,c):
        mat[i][j] = int (input(f'digite o elemento[{i},{j}]'))

print('-'*30)
print('numeros negativos')
print('-'*30)

for i in range(0,l):
    for j in range(0,c):
        if mat[i][j] < 0 :
            print(mat[i][j])

print('-'*30)
