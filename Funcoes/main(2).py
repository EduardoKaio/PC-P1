def primo(lista):
  cont_divisor=0
  divisores=[]
  print('A classificação é:')
  for j in lista:
    for k in range(1,j+1):
      if (j % k == 0):
        cont_divisor += 1
        divisores.append(k)
    if(cont_divisor>2):
      print(f'{j} não é primo, os divisores são: {divisores}')
    else:
      print(f'{j} é primo')
    cont_divisor=0
    divisores=[]

numero=int(input('Qual o valor de N?'))
lista=[]
print('Digite os valores: ')
for i in range(numero):
  valor=int(input())
  lista.append(valor)
primo(lista)
