n1 =float(input('primeira nota do aluno:'))
n2 = float(input('segunda nota do aluno:'))

nota = n1 + n2

print(f'nota final:{nota}')

if nota < 60.0 :
    print('aluno reprovado!')
else:
    print('aluno aprovado!')

 