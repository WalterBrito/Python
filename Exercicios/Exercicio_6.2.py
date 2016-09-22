# -*- coding: utf-8 -*-

"""
Faça um programa que percorra duas listas e gere uma 
terceira sem elementos repetidos.
"""

print(60 * "=")

l1 = []
l2 = []

print("Lista 1")
while True:
    lista1 = int(input("Digite (l1) ou (0 - sair): "))

    if lista1 < 0:
        break
    l1.append(lista1)

print("\nLista 2")
while True:
    lista2 = int(input("Digite (l2) ou (0 - sair): "))

    if lista2 < 0:
        break
    l2.append(lista2)


lista3 = []
l3 = l1[:]
l3.extend(l2)
x = 0

while x < len(l3):
    y = 0
    while y < len(lista3):
        if l3[x] == lista3[y]:
            break
        y += 1

    if y == len(lista3):
        lista3.append(l3[x])
    x += 1
x = 0

print("\nLista 3")
while x < len(lista3):
    print("%d: %d" % (x, lista3[x]))
    x += 1

print(60 * "=")
