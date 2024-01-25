l = int(input('quantas linhas terá cada matriz?:'))
c = int(input('quantas colunas terá cada matriz?:'))

matA = [[0 for x in range(c)]for x in range(l)]
matB = [[0 for x in range(c)]for x in range(l)]
soma = [[0 for x in range(c)]for x in range(l)]

print('matriz A')
print('-'*30)
for i in range(0,l):
    for j in range(0,c):
        matA[i][j]= int(input(f'elemento[{i},{j}]:'))
print('-'*30)

print('matriz B')
print('-'*30)
for i in range(0,l):
    for j in range(0,c):
        matB[i][j]= int(input(f'elemento[{i},{j}]:'))
print('-'*30)

for i in range(0,l):
    for j in range(0,c):
        soma[i][j] = matA[i][j] + matB[i][j]

print('matriz soma')
print('-'*30)

for i in range(0,l):
    print()
    for j in range(0,c):
        print(soma[i][j],end=' ')
    
