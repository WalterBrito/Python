# -*- coding: utf-8 -*-

"""
Escreva uma função que receba a base e a altura de um triãngulo
e retorne sua área (A = (base X altura)/2).
Valores esperados:
área_triângulo(6,9) == 27
área_triângulo(5,8) == 20
"""

print(60 * "=")


def área_triângulo(base, altura):
    return (base * altura) / 2

print("área_triângulo(6,9) == 27 -> resultado: %d" % área_triângulo(6, 9))
print("área_triângulo(8,8) == 20 -> resultado: %d" % área_triângulo(5, 8))

print(60 * "=")
