nota = float(input("Digite a nota: "))
while nota <0 or nota >10:
    print('Digite uma nota válida')
    nota = float(input("Digite a nota: "))
print(f"Nota registrada {nota}")
