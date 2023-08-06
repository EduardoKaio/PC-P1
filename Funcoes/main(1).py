def Saldo(saldo):
  return print(f'O seu saldo agora é de: {saldo}')

def Deposito(saldo):
  deposito=float(input('Qual o valor deseja depositar?'))
  saldo=saldo+deposito
  Saldo(saldo)
  return saldo

def Saque(saldo):
  sacar=float(input('Qual o valor deseja sacar?'))
  saldo=saldo-sacar
  Saldo(saldo)
  return saldo

def ExibeOpcoes():
  print('1 - SAQUE\n2 - DEPOSITO\n3 - SALDO\n4 - SAIR')
  opcao=int(input('Escolha: '))
  return opcao

def ProcessaOpcoes(opcao, saldo):
  if opcao==1:
    Saque(saldo)
  elif opcao==2:
    Deposito(saldo)
  elif opcao==3:
    Saldo(saldo)

def Principal():
    opcao = 0
    saldo = 1000
    while opcao!=4: 
      opcao = ExibeOpcoes()
      if opcao == 4:
        print('Processo encerrado')
        break
      elif (opcao!=1) and (opcao!=2) and (opcao!=3):
        print('Operação inválida')
      else:
        ProcessaOpcoes(opcao, saldo)

Principal()
    
    
    
    
    
    
    
    