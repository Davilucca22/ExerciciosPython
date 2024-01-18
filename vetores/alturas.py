n = int(input('quantas pessoas serao digitadas?:'))

nome = [0 for x in range(n)]
idade = [0 for x in range (n)]

soma = 0

for c in range(0,n):
    print(f'dados da {c+1}ª pessoa')
    print('-'*30)
    nome[c] = str(input('nome da pessoa:'))
    idade[c] = int (input('idade da pessoa:'))
    alt = float(input('altura da pessoa:'))
    soma = soma + alt
    print('-'*30)

media = soma / n

print(f'media de altura do grupo:{media:.2f}')

cont = 0 

for c in range(0,n):
    if idade[c] < 16:
        cont = cont + 1

abaixo = cont * 100 / n

print(f'pessoas com menos de 16 anos:{abaixo:.2f}%')

for c in range(0,n):
    if idade[c] < 16:
        print(nome[c])
