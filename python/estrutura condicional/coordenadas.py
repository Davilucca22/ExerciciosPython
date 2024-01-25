x = int(input('valor de X:'))
y = int(input('valor de Y:'))

if x > 0 and y > 0:
    print('Q1')
elif x < 0 and y > 0:
    print('Q2')
elif x < 0 and y < 0:
    print('Q3')
elif x > 0 and y < 0 :
    print('Q4')
elif x != 0 and y == 0:
    print('EIXO X')
elif x == 0 and y != 0:
    print('EIXO Y')
else:
    print('origem')