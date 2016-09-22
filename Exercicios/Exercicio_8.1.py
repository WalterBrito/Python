# -*- coding: utf-8 -*-

"""
Escreva uma função que retorne o maior de dois números.
Valores esperados:
máximo(5,6) == 6
máximo(2,1) == 2
máximo(7,7) == 7
"""


print(60 * "=")

def máximo(a, b):
    if a > b:
        return a
    else:
        return b

print("máximo(5,6) == 6 -> Maior: %d" % máximo(5, 6))
print("máximo(2,1) == 2 -> Maior: %d" % máximo(2, 1))
print("máximo(7,7) == 7 -> Maior: %d" % máximo(7, 7))

print(60 * "=")
