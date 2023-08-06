numero = int(input('Quantos alunos?'))

alunos = []

print('Digite os nomes dos alunos:')
for i in range(numero):
  nome = input()
  alunos.append(nome)

if numero % 2 != 0:
  for i in range(numero // 2):
    if i % 2 != 0:
      alunos[i], alunos[-(i+1)] = alunos[-(i+1)], alunos[i]
else:
  for i in range(numero // 2):
    if i % 2 == 0:
      alunos[i+1], alunos[-(i+1)] = alunos[-(i+1)], alunos[i+1]

print("Nova lista:")

for nome in alunos:
  print(nome)