# -*- coding: utf-8 -*-

"""
Faça um programa em que o usuário possa digitar, o inicio
e o fim da tabuada, em vez de começar com 1 e 10.
"""

print(60 * "=")

num = int(input("Digite um número: "))
inicio = int(input("Tabuada de: "))
fim = int(input("Até: "))

x = inicio
while x <= fim:
    print("%d x %d = %d" % (num, x, (num * x)))
    x += 1

print(60 * "=")
