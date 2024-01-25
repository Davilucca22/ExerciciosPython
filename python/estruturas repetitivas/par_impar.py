n = int(input('quantos numeros serao lidos?:'))

for c in range(0,n):
    x = int(input('digite um numero:'))
    if x == 0:
        print('nulo')

    elif x % 2 == 0:
        print('par',end=' ')
        if x > 0:
            print('positivo')
        else:
            print('negativo')
            
    else:
        print('impar',end=' ')
        if x > 0 :
            print('positivo')
        else:
            print('negativo')
