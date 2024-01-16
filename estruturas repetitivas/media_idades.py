idade = (int(input('digite as idades:')))

if idade < 0 :
   print('impossivel calcular!')
else:
    soma = 0
    cont = 0
    while idade > 0:
        soma = soma + idade
        cont = cont + 1
        idade = (int(input('digite as idades:')))
    media = soma / cont
    print('-'*30)
    print(f'media de idades:{media:.2f}')
    print('-'*30)

