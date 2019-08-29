"""Escreva um programa em Python que leia um vetor de números de tamanho t. Leia t previamente.
Em seguida, faça seu programa verificar quantos números iguais a 0 existem nele."""

tamanho_do_vetor = int(input("Digite o tamanho da lista: "))
vetor_numeros = []

for i in range(0, tamanho_do_vetor):
    numeros = input("Agora digite o número: ")
    vetor_numeros.append(numeros)
print(vetor_numeros)    
    
if 0 in vetor_numeros:
    print("Existem ", vetor_numeros.count(0), "na lista")
