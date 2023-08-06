
n1 = int(input('n1?'))
n2 = int(input('n2?'))
aux=0
impar=[]
cont_divisor=0
if n1 > n2:
  aux=n1
  n1=n2
  n2=aux

for i in range(n1,n2):
  for j in range(2,i):
    if (i % j == 0) and (i % 2 == 1):
      cont_divisor += 1
        
    if(cont_divisor>=1):
      impar.append(i)
      break
  cont_divisor=0

print(f'numeros ímpares não primos [{n1}-{n2}]: {str(impar)[1:-1]}' )






  
    
    
    
    
    