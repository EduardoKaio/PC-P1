def criptografar(palavra):
  lista_palavra=list(palavra)
  for i in range(len(lista_palavra)):
    if (lista_palavra[i]=='a') or (lista_palavra[i]=='b') or (lista_palavra[i]=='c') or (lista_palavra[i]=='d') or (lista_palavra[i]=='e'):
      del lista_palavra[i]
      lista_palavra.insert(i, '1')
    elif (lista_palavra[i]=='f') or (lista_palavra[i]=='g') or (lista_palavra[i]=='h') or (lista_palavra[i]=='i') or (lista_palavra[i]=='j'):
      del lista_palavra[i]
      lista_palavra.insert(i, '2')
    elif (lista_palavra[i]=='k') or (lista_palavra[i]=='l') or (lista_palavra[i]=='m') or (lista_palavra[i]=='n') or (lista_palavra[i]=='o'):
      del lista_palavra[i]
      lista_palavra.insert(i, '3')
    elif (lista_palavra[i]=='p') or (lista_palavra[i]=='q') or (lista_palavra[i]=='r') or (lista_palavra[i]=='s') or (lista_palavra[i]=='t') or (lista_palavra[i]=='u') or (lista_palavra[i]=='v') or (lista_palavra[i]=='w') or (lista_palavra[i]=='x') or (lista_palavra[i]=='y') or (lista_palavra[i]=='z'):
      del lista_palavra[i]
      lista_palavra.insert(i, '4')
    elif (lista_palavra[i]==' '):
      del lista_palavra[i]
      lista_palavra.insert(i, '5')
  
  for j in lista_palavra:
    palavra_encrip=print(j, end='')
  
  return palavra_encrip


palavra=str(input('Digite o texto: '))
criptografar(palavra)
