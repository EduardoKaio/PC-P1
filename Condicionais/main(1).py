numero = int(input('Digite um número: '))
resto_dias=0
semanas=0

#Dias menores que uma semana
if (numero >= 0) and (numero < 7):
  if numero == 0:
    print ('0 dias equivale à nenhum dia.')
  elif numero == 1:
    print (f'{numero} dia equivale à {numero} dia.')
  else:
    print (f'{numero} dias equivale à {numero} dias.')

#Dias maiores que uma semana
elif (numero>=7):
  semanas=int(numero/7)
  resto_dias=numero%7
  if (semanas == 1) and (resto_dias == 0): 
    print (f'{numero} dias equivale à {semanas} semana!')
  
  elif (semanas > 1) and (resto_dias == 0):
    print (f'{numero} dias equivale à {semanas} semanas!')
  
  elif (semanas == 1) and (resto_dias == 1): 
    print (f'{numero} dias equivale à {semanas} semana e {resto_dias} dia!')
  
  elif (semanas == 1) and (resto_dias > 1): 
    print (f'{numero} dias equivale à {semanas} semana e {resto_dias} dias!')
  
  elif (semanas > 1) and (resto_dias == 1): 
    print (f'{numero} dias equivale à {semanas} semanas e {resto_dias} dia!')
  
  elif (semanas > 1) and (resto_dias > 1): 
    print (f'{numero} dias equivale à {semanas} semanas e {resto_dias} dias!')
  
    
    
    
    