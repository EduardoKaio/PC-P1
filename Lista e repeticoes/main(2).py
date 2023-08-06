numero_jogadores=int(input('Quantidade de jogadores?'))
saque,bloq,ataque,saque_equipe,bloq_equipe,ataque_equipe=0, 0, 0, 0, 0, 0
lista=[]
lista_dividida=[]
print('Digite os dados para cada jogador:')
for i in range(numero_jogadores):
  jogador=str(input())
  lista.append(jogador)

for j in range(numero_jogadores):
  lista_dividida=lista[j].split()
  for k in range(7):
    match k:
      case 1:
        saque=saque+int(lista_dividida[1])
      case 2:
        bloq=bloq+int(lista_dividida[2])
      case 3:
        ataque=ataque+int(lista_dividida[3])
      case 4:
        saque_equipe=saque_equipe+int(lista_dividida[4])
      case 5:
        bloq_equipe=bloq_equipe+int(lista_dividida[5])
      case 6:
        ataque_equipe=ataque_equipe+int(lista_dividida[6])
print('As estatísticas do jogo são as seguintes:')
print(f'Pontos de Saque: {round(((saque_equipe/saque)*100), 2)}%')
print(f'Pontos de Bloqueio:: {round(((bloq_equipe/bloq)*100), 2)}%')
print(f'Pontos de Ataque:: {round(((ataque_equipe/ataque)*100), 2)}%')

  