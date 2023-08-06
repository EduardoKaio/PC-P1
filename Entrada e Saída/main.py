a = int(input('Valor lógico de A eh: '))
b = int(input('Valor lógico de B eh: '))
invalido = False

if a == 1:
  a=True
elif a == 0:
  a=False
else:
  invalido = True
  print('Valor de A inválido')
  
if b == 1:
  b=True
elif b == 0:
  b=False
else:
  invalido = True
  print('Valor de B inválido')

if invalido == False:
  if a and b == True:
    print('A AND B eh: True')
  elif a and b == False:
    print('A AND B eh: False')
if invalido == False:
  if a or b == True:
    print('A OR B eh: True')
  elif a or b == False:
    print('A OR B eh: False')