primeiro = int(input('primeiro valor:'))
segundo  = int(input('segundo valor:'))
terceiro = int(input('terceiro valor:'))

if primeiro < segundo and primeiro < terceiro:
    print(f'menor:{primeiro}')
elif segundo < terceiro:
    print(f'menor:{segundo}')
else:
    print(f'menor:{terceiro}')
