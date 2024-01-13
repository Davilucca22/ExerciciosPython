produto = float(input('valor unitario do produto:'))
qtd = int(input('quantidade:'))
dindin = float(input('dinheiro recebido:'))

valorTotal = produto * qtd
print('-'*30)
print(f'valor total da compra = R${valorTotal}')
print('-'*30)
print()
if dindin >= valorTotal:
    troco = dindin - valorTotal
    print('-'*30)
    print(f'troco = R${troco:.2f}')
    print('-'*30)
else:
    falta = valorTotal - dindin
    print('-'*30)
    print(f'dinheiro insuficiente,faltam: R${falta:.2f}')
    print('-'*30)
