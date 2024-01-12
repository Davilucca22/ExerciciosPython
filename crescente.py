print('digite dois numeros:')
n1 = int(input(''))
n2 = int(input(''))

if n1 < n2 :
    print('crescente')
else:
    print('decrescente')

while True:
    print('digite outros dois numeros:')
    n1 = int(input(''))
    n2 = int(input(''))

    if n1 < n2 :
        print('crescente')
    elif n1 > n2 :
        print('decrescente')
    else:
        break
