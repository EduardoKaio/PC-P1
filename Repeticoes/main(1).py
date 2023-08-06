n = int(input('n?'))

if (n > 0) and (n < 10):
  for i in range (1,n+1):
    for j in range (0,i):
      print(i, end='')
    print()
else:
  print('Digite um número entre 0 e 10')
