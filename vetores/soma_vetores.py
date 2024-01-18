n = int(input('quantos elemntos cada vetor terá?:'))

a = [0 for x in range(n)]
b = [0 for x in range(n)]
d = [0 for x in range(n)]

print('-'*30)
print('vetor A:')
print('-'*30)
for c in range(0,n):
    a[c] = int(input('digite um numero:'))
print('-'*30)

print('vetor B:')
print('-'*30)
for c in range(0,n):
    b[c] = int(input('digite um numero:'))
print('-'*30)

print('vetor resultante:')
print('-'*30)
for c in range(0,n):
    d[c] = (a[c] + b[c])
    print(d[c])
print('-'*30)