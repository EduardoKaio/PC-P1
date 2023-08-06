a = str(input('Digite o texto A: '))
b = str(input('Digite o texto B: '))
print('tamanho(A) - tamanho(B) = ', (len(a)-len(b)))
print('A + B = ', a+b)
if a.count(b) >= 1:
  print('A contém B = True')
else:
  print('A contém B = False')
if b.count(a) >= 1:
    print('B contém A = True')
else:
  print('B contém A = False')
print('Primeira letra de A = ', a[0])
print('Primeira letra de B = ', b[0])
print('Última letra de A = ', (a[len(a)-1]))
print('Última letra de B = ', (b[len(b)-1]))