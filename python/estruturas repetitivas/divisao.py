n = int(input('quantos casos vai digitar?:'))

for c in range(0,n):
    num = int(input('digite o numerador:'))
    den = int(input('digite o denominador:'))
    if den == 0:
        print('-'*30)
        print('divisao impossivel!')
        print('-'*30)
    else:
        print('-'*30)
        print(f'divisao = {num/den}')
        print('-'*30)