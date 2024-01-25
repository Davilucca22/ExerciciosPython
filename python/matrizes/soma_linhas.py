l = int(input('quantidade de linhas da matriz:'))
c = int(input('quantidade de colunas da matriz:'))

mat = [[0 for x in range(c)]for x in range(l)]
vet = [0 for x in range(l)]

for i in range(0,l):
    print(f'digite os elementos da {i+1}º linha:')
    for j in range(0,c):
        mat[i][j] = int(input(' '))


print('-'*30)
print('vetor resultante')
print('-'*30)

for i in range(0,l):
    for j in range(0,c):
        vet[i] = vet[i]  + mat[i][j]
    print(vet[i])

print('-'*30)