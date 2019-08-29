"""Escreva um programa em Python que leia um vetor de 10 palavras e mostre-as na ordem inversa de leitura."""

lista_palavras = []

while True:
    palavra = input("Digite 10 palavras: ")
    if len(lista_palavras) == 10:
        break
    lista_palavras.append(palavra)
    
    
print(lista_palavras[::-1])    
    