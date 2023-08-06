nome_atleta=str(input('Nome do Atleta: '))
nota=[]
resposta = 0
maior=0
menor=0
for i in range(7):
  resposta = float(input(f'Nota_{i+1}:'))
  nota.append(resposta)

maior=max(nota)
menor=min(nota)
nota.remove(max(nota))
nota.remove(min(nota))
media=sum(nota)/5
print(f'Resultado final:\nAtleta: {nome_atleta}\nMelhor nota: {maior}\nPior nota: {menor}\nMédia: {round(media, 2)}')


