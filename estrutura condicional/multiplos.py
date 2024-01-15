print('digite dois numeros inteiros')
print('-'*35)

n1 = int(input('primeiro numero:'))
n2 = int(input('segundo numero:'))

if n2 > n1 :
    troca = n1
    n1 = n2 
    n2 = troca
print('-'*35)
if n1 % n2 == 0 :
    print('sao multiplos!')
else:
    print('nao sao multiplos')
print('-'*35)