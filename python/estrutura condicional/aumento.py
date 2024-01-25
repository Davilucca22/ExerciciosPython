print('-'*35)
salarioAT = float(input('digite seu salario atual:'))

if salarioAT <= 1000:
    porcentagem = salarioAT * 20 / 100
    novoSalario = salarioAT + porcentagem

elif salarioAT <= 3000:
    porcentagem = salarioAT * 15 / 100
    novoSalario = salarioAT + porcentagem

elif salarioAT  <= 8000:
    porcentagem = salarioAT * 10 / 100
    novoSalario = salarioAT + porcentagem

else:
    porcentagem = salarioAT * 5 / 100
    novoSalario = salarioAT + porcentagem

print('-'*35)
print(f'novo salario:R${novoSalario}')
print(f'aumento:{porcentagem}')
if salarioAT <= 1000:
    print('porcentagem: 20%')
elif salarioAT <= 3000:
   print('porcentagem: 15%')
elif salarioAT  <= 8000:
    print('porcentagem: 10%')
else:
   print('porcentagem: 5%')
print('-'*35)