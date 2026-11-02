nome = input("Digite seu nome: ")
contador = 0
for letra in nome:
    contador = contador + 1
while contador <=3:
    print('Digite um nome válido')
    nome = input("Digite seu nome: ")
print(f"Nome registrado, {nome}")
idade = float(input("Digite sua idade: "))
while idade <0 or idade >150:
    print('Digite uma idade válida')
    idade = float(input("Digite sua idade: "))
print(f'Idade registrada, {idade}')
