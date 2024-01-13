precoUni = float(input('preço unitario do produto:'))
qtd = int(input('quantidade:'))
dindin = float(input('dinheiro recebido:'))
precoTotal = precoUni * qtd
total = dindin - precoTotal
print('-'*30)
print(f'troco:R${total:.2f}')
print('-'*30)