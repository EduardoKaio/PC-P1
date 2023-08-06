qnt_numeros=int(input('Qual o N?'))
numero=0
lista=[]

print('Digite os valores')
for i in range(1, qnt_numeros+1):
  numero = int(input(''))
  lista.append(numero)

op = int(input('Qual a op?'))
a = int(input('Qual o A?'))
b = int(input('Qual o b?'))

if (op == 0):
  print(f'{lista[a-1]} + {lista[b-1]} = {lista[a-1]+lista[b-1]}')
elif (op == 1):
  print(f'{lista[a-1]} * {lista[b-1]} = {lista[a-1]*lista[b-1]}')
else:
  print('Digite uma operação válida')
  