lista = [0,-14,5,100,-80,40,-14]

print("lista:\n")
for i in lista:
    print(i, "\n")

print("\nlista invertida:\n")
lista.reverse()
for i in lista:
    print(i, "\n")

print("\n5 adicionada:\n")
lista.reverse()
lista.append(5)
for i in lista:
    print(i, "\n")

print("\nAdiciona 100 na posição 4(indice 3):\n")
lista.insert(4, 100)
for i in lista:
    print(i, "\n")

print("\n Imprimir a quantidade que cada elemento aparece na lista\n ")
from collections import Counter
contador = Counter(lista)
for elemento, quantidade in contador.items():
    print(f"O elemento {elemento} aparece {quantidade} vezes na lista.")


print("\nOrde crescente:\n")
for i in lista:
    lista.sort()
    print(i, "\n")

print("\n orde decrescente:\n")
lista.sort(reverse=True)
for i in lista:
    print(i, "\n")
