glicose = float(input('medida da glicose:'))

if glicose <= 100:
    print('normal')
elif glicose <= 140:
    print('elevado')
else:
    print('diabetes')