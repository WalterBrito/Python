# -*- coding: utf-8 -*-

"""
Escreva um programa que leia um valor em metros e o exiba
convertido em milimetros.
"""

print(60 * "=")
metros = float(input("Digite um valor em metros: "))

milimetros = metros * 1000

print("%.1f metros em milimetros e %d." % (metros, milimetros))
print(60 * "=")
