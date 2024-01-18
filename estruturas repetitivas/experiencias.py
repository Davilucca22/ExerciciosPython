n = int(input('quantos casos de teste serao digitados?:'))

totalCobaias = 0
totalRatos = 0
totalCoelhos = 0 
totalSapos = 0

for c in range(0,n):
    quant = int(input('quantidade de cobaias:'))
    tipo = str(input('tipo de cobaias:').upper)

    totalCobaias = totalCobaias + quant

    if tipo == 'C':
        totalCoelhos = totalCoelhos + quant
    elif tipo == 'R':
        totalRatos = totalRatos + quant
    elif tipo == 'S':
        totalSapos = totalSapos + quant

Pratos = totalRatos * 100 / totalCobaias
psapos = totalSapos * 100 / totalCobaias
pcoelhos = totalCoelhos * 100 / totalCobaias

print('-'*30)
print(f'total de cobaias = {totalCobaias}')
print('-'*30)
print(f'total de ratos = {totalRatos}')
print(f'percentual de ratos = {Pratos:.2f}%')
print('-'*30)
print(f'total de sapos = {totalSapos}')
print(f'percentual de sapos = {psapos:.2F}%')
print('-'*30)
print(f'total de coelhos = {totalCoelhos}')
print(f'percentual de coelhos = {pcoelhos:.2f}%')
print('-'*30)
