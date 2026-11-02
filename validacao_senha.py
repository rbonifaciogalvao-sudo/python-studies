senha = int(input("Digite a senha: "))

while senha != 1234:
  print ("Senha incorreta, digite novamente")
  break
senha = int(input("Digite a senha: "))
while senha == 1234:
  print ("Acesso liberado.")
  break
