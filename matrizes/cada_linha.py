o = int(input('qual a ordem da matriz?:'))

mat = [[0 for x in range(o)]for x in range(o)]
maiorlinha = []

for i in range(0,o):
    for j in range(0,o):
        mat[i][j] = int(input(f'elemento[{i},{j}]:'))

for i in range(0,o):
    maior = mat[i][0]
    for j in range(1,o):
        if maior < mat[i][j] :
           maior = mat[i][j]
    maiorlinha.append(maior)

print('-'*30)
print('maior elemento de cada linha')
print('-'*30)

for c in range(0,o):
    print(maiorlinha[c])