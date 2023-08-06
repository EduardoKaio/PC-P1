n1 = int(input('Digite n1:'))
n2 = int(input('Digite n2:'))
aux=0
if n1 > n2:
  aux=n1
  n1=n2
  n2=aux

if (n1<1) or (n2>10):
  print('Digite os números entre 1 e 10')
else:
  for i in range(n1, n2+1):
    print(f'=-=-=-= Tabuada de {i} =-=-=-=')
    for j in range(1, 11):
      print(f'{i} x {j} = {i*j}')

      
      
      
      
      
      