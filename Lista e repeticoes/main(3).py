import math
numero=int(input('Qual o valor do N?'))
lista=[]
dados_anterior, quartil_1, quartil_3, mediana, inferior, superior, intervalo=0, 0, 0, 0, 0, 0, 0
crescente=True
if (numero<=2):
  print('O número tem que ser maior do que 2!!')
else:
  dados=input('Digite os dados: ').split(' ')
  for i in range(numero):
    if i>0:
      if (dados[i]<dados[i-1]):
        print('Erro! Conjunto tem de estar em ordem crescente')
        crescente=False
        break
      
  if crescente==True:   
    quartil_1=dados[int(round(numero-1)/4)]
    quartil_3=dados[int(round(((numero-1)*3)/4))]
    inferior=dados[0]
    intervalo=float(dados[int(round(((numero-1)*3)/4))])-float(dados[int(round(numero-1)/4)])
    if numero%2==1:
      mediana=float(dados[int(numero/2)])
    else:
      mediana=float((float((dados[int(numero/2)]))+float((dados[int((numero/2)-1)])))/2)
      
    if int(dados[(numero-1)])>((intervalo*1.5)+mediana):
      superior=dados[len(dados)-2]
    else:
      superior=dados[len(dados)-1]
  
    print('Limite inferior: ', inferior)
    print('1o quartil: ', quartil_1)
    print('Mediana: ', mediana)
    print('3o quartil: ', quartil_3)
    print('Limite superior: ', superior)