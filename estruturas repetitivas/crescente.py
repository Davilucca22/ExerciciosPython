print('-'*30)
print('digite dois numeros')
print('-'*30)

n1 = int(input('primeiro numero:'))
n2 = int(input('segundo numero:'))

if n1 > n2 :
    print('decrescente')
else:
    print('crescente')

while True:
    n1 = int(input('primeiro numero:'))
    n2 = int(input('segundo numero:'))

    if n1 > n2 :
      print('decrescente')
    elif n1 < n2:
      print('crescente')
    else:
       break
