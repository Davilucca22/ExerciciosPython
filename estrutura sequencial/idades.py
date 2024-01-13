nome1 = str(input('nome da primeira pessoa:'))
idade1 = int(input('idade da primeira pessoa:'))

nome2 = str(input('nome da segunda pessoa:'))
idade2 = int(input('idade da segunda pessoa:'))

media = (idade1 + idade2) / 2

print(f'a media de idade entre {nome1} e {nome2} é de {media:.1f}')