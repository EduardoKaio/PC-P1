n1 = int(input('n1?'))
n2 = int(input('n2?'))
n3 = int(input('n3?'))
menor=0
maior=0
meio=0
if (n1 == n2) and (n2 == n3):
  print('todos são iguais a ', n1)
elif (n1 == n2) or (n2 == n3) or (n1 == n3):
  if(n1 > n2) and (n1 > n3):
    maior = n1
  elif(n2 > n1) and (n2 > n3):
    maior = n2
  else:
    maior = n3
  if n1 < maior:
    menor=n1
  elif n2 < maior:
    menor=n2
  else:
    menor=n3
  print('maior: ', maior)
  print('Menores: ', menor)
  print('Não há elementos do meio')
else:
  #maior
  if(n1 > n2) and (n1 > n3):
    maior = n1
  elif(n2 > n1) and (n2 > n3):
    maior = n2
  else:
    maior = n3
  #menor
  if(n1 < n2) and (n1 < n3):
    menor = n1
  elif(n2 < n1) and (n2 < n3):
    menor = n2
  else:
    menor = n3
  #meio
  if((n1 > n2) and (n1 < n3)) or ((n1 < n2) and (n1 >n3)):
    meio = n1
  elif((n2 > n1) and (n2 < n3)) or ((n2 < n1) and (n2 >n3)):
    meio = n2
  else:
    meio = n3
  print(f'Maior: {maior}\nMenor: {menor}\nMeio: {meio}')