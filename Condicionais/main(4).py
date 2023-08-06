texto_completo=''
texto1 = str(input('Texto 1?'))
texto2 = str(input('Texto 2?'))
texto3 = str(input('Texto 3?'))
maior=''
meio=''
menor=''

if (texto1<texto2) and (texto1<texto3):
  if (texto2<texto3):
    maior=texto1
    meio=texto2
    menor=texto3
  else:
    maior=texto1
    meio=texto3
    menor=texto2
elif (texto2<texto1) and (texto2<texto3):
  if (texto1<texto3):
    maior=texto2
    meio=texto1
    menor=texto3
  else:
    maior=texto2
    meio=texto3
    menor=texto1
elif (texto3<texto1) and (texto3<texto2):
  if (texto1<texto2):
    maior=texto3
    meio=texto1
    menor=texto2
  else:
    maior=texto3
    meio=texto2
    menor=texto1
print(f'1o. {maior}\n2o. {meio}\n3o. {menor}')