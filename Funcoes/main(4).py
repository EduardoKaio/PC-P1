import math

def valoresLidos():
  lista=[]
  numero=int(input('N?'))
  print('Quais os valores?')
  for i in range(numero):
    valor=int(input())
    lista.append(valor)
  return lista

def parProximo(lista):
  distancia=0
  for j in range(len(lista)):
    for k in range(len(lista)):
      if lista[j]!=lista[k]:
        if (j==0) and (k==1):
          distancia=abs(lista[j]-lista[k])
        elif abs(lista[j]-lista[k])<distancia:
          distancia=abs(lista[j]-lista[k])
          valor1=lista[j]
          valor2=lista[k]

  return print(f'Par mais próximo: {valor1} e {valor2}')

lista=valoresLidos()
parProximo(lista)





