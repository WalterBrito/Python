# -*- coding: utf-8 -*-

"""
Faça um programa que leia duas listas e que gere uma 
terceira com os elementos das duas primeiras.
"""

print(60 * "=")

l1 = []
l2 = []
l3 = []

print("Lista 1")
while True:
    lista1 = int(input("Digite (l1) ou (0 - sair): "))

    if lista1 < 0:
        break
    l1.append(lista1)

print("Lista 2")
while True:
    lista2 = int(input("Digite (l2) ou (0 - sair): "))

    if lista2 < 0:
        break
    l2.append(lista2)

l3.append(l1[:])
l3.extend(l2)

print("l1 =", l1)
print("l2 =", l2)
print("l3 =", l3)

print(60 * "=")
