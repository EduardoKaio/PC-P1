
n1 = int(input('n1?'))
n2 = int(input('n2?'))
aux=0
cont_primo=0
cont_divisor=0

if n1 > n2:
  aux=n1
  n1=n2
  n2=aux

for i in range(n1,n2+1):
  for j in range(2,i):
    if (i % j == 0):
      cont_divisor += 1
  
  if(cont_divisor==0):
    cont_primo += 1
  cont_divisor=0

print(f'Existem {cont_primo} numeros primos entre {n1} e {n2}')







  
    
    
    
    
    