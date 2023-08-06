texto = str(input('texto?'))
i1 = int(input('i1?'))
i2 = int(input('i2?'))
aux=0
if i1 > i2:
  aux = i1
  i1 = i2
  i2 = aux

if (i1 >= len(texto)) or (i2 >= len(texto)):
  print('Os valores tem que ser menores do que o tamanho do texto')
else:
  print('Partes')
  for (i=0; i<i1;i++):
    print