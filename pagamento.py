nome = str(input('nome:'))
valorhora = float(input('valor por hora:'))
trabalho = float(input('horas tabalhadas:'))
pag = valorhora * trabalho
print('-'*30)
print(f'o pagamento para {nome} deve ser de R${pag}')
print('-'*30)