n = int(input('serao digitados quantos produtos?:'))

nome = [0 for x in range(n)]
pcompra = [0 for x in range(n)]
pvenda = [0 for x in range(n)]
porcentagemlucros= [0 for x in range(n)]

for c in range(0,n):
    print(f'produto {c+1}')
    nome[c] = str(input('nome:'))
    pcompra[c] = float(input('preco de compra:'))
    pvenda[c] = float(input('preco de venda:'))


for c in range(0,n):
    porcentagemlucros[c] = (pvenda[c] - pcompra[c]) / pcompra[c] * 100

abaixo = 0
entre = 0
acima = 0

for c in range(0,n):
    if porcentagemlucros[c] < 10:
        abaixo = abaixo + 1
    elif porcentagemlucros[c] < 20:
        entre = entre + 1 
    else:
        acima = acima + 1

tcompra = 0
tvenda = 0

for c in range(0,n):
    tcompra = tcompra + pcompra[c]

for c in range(0,n):
    tvenda = tvenda + pvenda[c]

ltotal = tvenda - tcompra

print()
print('relatorio de lucros')
print('-'*30)
print(f'lucro abaixo de 10% = {abaixo}')
print(f'lucro entre 10% e 20% = {entre}')
print(f'lucro acima de 20% = {acima}')
print(f'valor total de compra R${tcompra}')
print(f'valor total de venda R${tvenda}')
print(f'lucro total R${ltotal}')
print('-'*30)