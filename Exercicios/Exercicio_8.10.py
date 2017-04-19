# -*- coding: utf-8 -*-

"""
Escreva uma função para validar uma variável string. Essa Função recebe
como parâmetro a string, o número minimo e máximo de caracteres. Retorne
verdadeiro se o tamanho da string estiver entre o valores de máximo e
minimo, e falso em caso contrário.
"""


print(60 * "=")


def string(s, minimo, máximo):
    tamanho = len(s)
    return minimo <= tamanho <= máximo

print(string("", 1, 5))
print(string("ABC", 2, 5))
print(string("ABCEFG", 3, 5))
print(string("ABCEFG", 1, 10))

print(60 * "=")
