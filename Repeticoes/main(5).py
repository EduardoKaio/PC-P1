n = int(input('n?'))
resultado=0
aux=0
for i in range(1,n):
  resultado = i*(i+1)*(i+2)
  if (resultado==n):
    aux=+1
if aux==1:
  print('É triangular')
else:
  print('Não é triangular')