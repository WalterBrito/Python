# -*- coding: utf-8 -*-

"""
Crie um programa que faça uma tabuada, no mesmo formato
formato: 2x1 = 2, 2x2 = 4,...
"""

print(60 * "=")
num = int(input("Digite um número: "))

x = 1
while x <= num:
    print("%d x %d = %d" % (num, x, num * x))
    x += 1

print(60 * "=")
