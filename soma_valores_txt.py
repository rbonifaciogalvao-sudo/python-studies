with open("valores.txt", "w") as arquivo:
     arquivo.write("2\n4\ntexto\n")

total = 0
with open("valores.txt", "r") as arquivo:
     for linha in arquivo:
         try:
              total = total + int(linha)
         except ValueError:
             total = total + 1
resultado = total
print (resultado)
