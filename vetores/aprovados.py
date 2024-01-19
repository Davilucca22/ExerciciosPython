n = int(input('quantos alunos serao digitados:'))

nome = [0 for x in range(n)]
notaUm = [0 for x in range(n)]
notaDois = [0 for x in range(n)]
notaFinal = [0 for x in range(n)]

for c in range(0,n):
    print(f'informaçoes do {c+1}º aluno')
    nome[c] = str(input('nome:'))
    notaUm[c] = float(input('nota 1º semestre:'))
    notaDois[c] = float(input('nota 2º semestre:'))

soma = 0

for c in range(0,n):
    soma = notaUm[c] + notaDois[c]
    media = soma / 2
    notaFinal[c] = media

print('-'*30)
print('alunos aprovados:')
for c in range(0,n):
    if notaFinal[c] >= 6.0:
        print(nome[c])
print('-'*30)

