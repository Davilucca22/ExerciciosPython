cod = int(input('digite qual tipo de combustivel voce prefere\n[1]alcool\n[2]gasolina\n[3]diesel\n[4]parar\n:'))

alcool = 0
gasolina = 0 
diesel = 0

while True:
   if cod == 1 :
      alcool = alcool + 1
   elif cod == 2:
      gasolina = gasolina + 1
   elif cod == 3 :
      diesel = diesel + 1
   elif cod == 4:
      break
   cod = int(input('digite qual tipo de combustivel voce prefere\n[1]alcool\n[2]gasolina\n[3]diesel\n[4]parar\n:'))   

print(f'alcool:{alcool}')
print(f'gasolina:{gasolina}')
print(f'diesel:{diesel}')
 