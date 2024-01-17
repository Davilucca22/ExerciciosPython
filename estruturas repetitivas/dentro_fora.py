n = int(input('quantos numeros voce vai digitar?:'))

dentro = 0
fora = 0
for c in range(0,n):
    x = int(input('digite um numero:'))
    if x >= 10 and x <= 20:
        dentro = dentro + 1
    else:
        fora = fora + 1

print('-'*30)
print(f'numeros dentro do intervalo [10,20] : {dentro}')
print('-'*30)
print(f'numeros fora do intervalo [10,20] : {fora}')
print('-'*30) 