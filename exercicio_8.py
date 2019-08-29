"""Faça uma função um programa em Python que simula um lançamento de dados.
Lance o dado 100 vezes e armazene os resultados em um vetor.
Depois, mostre quantas vezes cada valor foi conseguido.
Dica: use um vetor de contadores (1-6) e uma função do módulo 'random' de
Python para gerar números aleatórios, simulando os lançamentos dos dados."""


from random import randrange

dado = []

for i in range(0,100):
    valor_dado = str(randrange(1,7,1))
    dado.append(valor_dado)
    
for i in range(1,7):
    ocorencia_um = dado.count(str(i))
    print(f"O número {i} aconteceu {ocorencia_um} vezes")
