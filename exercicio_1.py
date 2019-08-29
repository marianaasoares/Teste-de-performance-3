"""Usando Python, faça o que se pede (código e printscreen):
Crie uma lista vazia;
Adicione os elementos: 1, 2, 3, 4 e 5,  usando append();
Imprima a lista;
Agora, remova os elementos 3 e 6 (não esqueça de checar se eles estão na lista);
Imprima a lista modificada;
Imprima também o tamanho da lista usando a função len();
Altere o valor do último elemento para 6 e imprima a lista modificada."""

lista = []
lista.extend((1,2,3,4,5)) #Fiz com extend porque achei masi fácil do que fazer um for 
print("Lista preenchida: ", lista)

lista.remove(5)
if 6 in lista:
    lista.remove(6)
    
print("Lista modificada pela 2ª vez: ", lista)

print("Tamanho da Lista: ", len(lista))

lista.append(6)
print("Lista com o último Elemento sendo o 6: ", lista)