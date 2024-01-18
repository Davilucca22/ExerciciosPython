n = int(input('quantos casos voce vai digitar?:'))

for c in range(0,n):
    print('digite os tres numeros:')
    n1 = float(input())
    n2 = float(input())
    n3 = float(input())

    ponderada = ((n1 * 2) + (n2 * 3) + (n3 * 5)) / 10
    
    print(f'media ponderada = {ponderada:.1f}')
