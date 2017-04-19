# -*- coding: utf-8 -*-

"""
Escreva uma função que receba uma string  e uma lista. A função deve
comparar a string passada com os elementos da lista, também passada
como parâmetro. retorne verdadeiro se a string for encontrada dentro
da lista, e falso em caso contrário.
"""


print(60 * "=")


def string(s, lista):
    return s in lista

l = ["AB", "CD", "EF", "FG"]

print(string("AB", l))
print(string("CD", l))
print(string("EF", l))
print(string("FG", l))
print(string("XYZ", l))


print(60 * "=")
