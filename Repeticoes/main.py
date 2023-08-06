n=int(input('Número de termos: '))
acumulador=1
resultado=0
proximo=0
anterior_1=1
anterior_2=0

print('Série de Fibonacci: ', end='')
for i in range(n):
  resultado=anterior_1+anterior_2
  anterior_2=anterior_1
  anterior_1=resultado
  
  if i==0:
    resultado=1
    anterior_1=1
    anterior_2=0
  print(resultado, end=' ')

