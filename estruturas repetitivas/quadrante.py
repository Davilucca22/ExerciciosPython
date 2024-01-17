print('-'*30)
print('digite os valores da coordenadas X e Y.')
print('-'*30)

x = int(input('ponto X:'))
y = int(input('ponto y:'))

while x != 0 and y != 0 : 
    if x > 0 and y > 0:
        print('quadrante 1')
    elif x < 0 and y > 0:
        print('quadrante 2')
    elif x < 0 and y < 0 :
        print('quadrante 3')
    elif x > 0 and y < 0:
        print('quadrante 4')

    x = int(input('ponto X:'))
    y = int(input('ponto y:'))
