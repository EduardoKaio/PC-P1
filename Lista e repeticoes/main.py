numero = int(input('Quantos nomes?'))
nome=''
lista=[]
for i in range(1, numero+1):
  nome = str(input(''))
  lista.append(nome)
print('Você digitou:')
for j in lista[::-1]:
  print(j)
