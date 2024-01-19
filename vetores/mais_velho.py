n = int(input('quantas pessoas voce vai digitar?:'))

nome = [0 for x in range(n)]
idade = [0 for x in range(n)]

for c in range(0,n):
    print(f'dados da {c+1}ª pessoa')
    nome[c] = str(input('nome:'))
    idade[c] = int(input('idade:'))

maior = idade[0] 
pos = 0

for c in range(0,n):
    if idade[c] > maior:
        maior = idade[c]
        pos = c

print(f'pessoa mais velha : {nome[pos]}')
