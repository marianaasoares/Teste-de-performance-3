"""Escreva um programa em Python que leia diversas frases até a palavra “Sair” ser digitada.
Indique quais frases apresentam a palavra “eu”"""

frases = []
palavra = ["eu"]

print("Escreva frases abaixo, caso queira que o programa pare só digitar 'Sair'. ")


while True: 
  frase = input("Digite a frase: ")
  if frase == "Sair":
    break
  frases.append(frase)

print(frases)  
for frase in frases:
  if "eu" in frase:
    print(frase)