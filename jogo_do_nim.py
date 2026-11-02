# Vez do jogador
jogador = True
print("Seja Bem Vinda ao Jogo do Nim")

# jogador escolhe a quatidade de peças que quer jogar e tirar

pecas = int(input("Com quantas peças você quer jogar? "))

while pecas > 0:
  if jogador:
    pecas_jogador = int(input("Quantas peças você quer tirar? "))

# Quantidade de peças que não podem ser tiradas

    while pecas_jogador > pecas or pecas_jogador > 3 or pecas_jogador <= 0:
      print("Jogada Inválida")
      pecas_jogador = int(input("Quantas peças você quer tirar? "))

# Peças tiradas e restantes

    pecas -= pecas_jogador
    print("Você tirou", pecas_jogador, "peças. Restam", pecas)

# Se a quatidade de peças for =0 o jogador ganha

    if pecas == 0:
      print("Você Ganhou!")
      break

# Estratégia usada pelo computador

    jogador = False

# Se for múltiplo de 4, tira 1

  else:
    if pecas % 4 == 0:
      pecas_computador = 1
    else:

 # Se não, tira o resto da divisão por 4

      pecas_computador = pecas % 4

    pecas -= pecas_computador

# Peças tiradas e restantes

    print("Computador tirou", pecas_computador, "peças. Restam", pecas)

# Se a quatidade de peças for =0 o computador ganha

    if pecas == 0:
      print("Computador Ganhou!")
      break

    jogador = True
