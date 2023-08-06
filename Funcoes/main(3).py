def imprimePartes(lista, separador):
  partes = []
  sublista = []
  
  for elemento in lista:
    if elemento == separador:
      if sublista:
        partes.append(sublista)
        sublista = []
    else:
      sublista.append(elemento)
 
  if sublista:
    partes.append(sublista)
  
  if partes:
    for parte in partes:
      lista_formatada = ' '.join(str(item) for item in parte)
      print(lista_formatada)
  else:
    print('Nenhuma')

n = int(input('N?'))
lista = []

print('Qual a sequência?')
for i in range(n):
  valor = int(input())
  lista.append(valor)

separador = int(input('Qual o elemento separador?'))

print('Sequências resultantes:')
imprimePartes(lista, separador)
