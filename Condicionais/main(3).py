n1 = float(input('Digite o Primeiro número:'))
n2 = float(input('Digite o Segundo número:'))
operacao = str(input('Digite a operação a realizar [+,-,* ou /]: '))

if operacao == '+':
  print(f'A soma de {n1} + {n2} é: {n1+n2}')
elif operacao == '-':
  print(f'A subtração de {n1} - {n2} é: {n1-n2}')
elif operacao == '*':
  print(f'A multiplicação de {n1} * {n2} é: {n1*n2}')
elif operacao == '/':
  print(f'A divisão de {n1} / {n2} é: {n1/n2}')
else:
  print('Operação inválida!')