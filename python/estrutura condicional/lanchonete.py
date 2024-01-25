n1 = 5.00
n2 = 3.50
n3 = 4.80
n4 = 8.90
n5 = 7.32

cod = int(input('codigo do produto:'))
qtd = int(input('quantidade comprada:'))

if cod == 1 :
    total = n1 * qtd
    print('-'*35)
    print(f'total a pagar:R${total:.2f}')
    print('-'*35)
elif cod  == 2:
    total = n2 * qtd
    print('-'*35)
    print(f'total a pagar:R${total:.2f}')
    print('-'*35)
elif cod == 3 :
    total = n3* qtd
    print('-'*35)
    print(f'total a pagar:R${total:.2f}')
    print('-'*35)
elif cod == 4:
    total = n4 * qtd
    print('-'*35)
    print(f'total a pagar:R${total:.2f}')
    print('-'*35)
elif cod == 5:
    total = n5 * qtd
    print('-'*35)
    print(f'total a pagar:R${total:.2f}')
    print('-'*35)
else:
    print('valor invalido!')
