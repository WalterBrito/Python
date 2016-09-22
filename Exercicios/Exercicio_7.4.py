# -*- coding: utf-8 -*-

"""
Escreva um programa que leia uma string e imprima quantas
vezes cada caractere aparece nessa string.

String: TTAAC

Resultado:

T: 2x
A: 2x
C: 1x
"""

print(60 * "=")

s = input("Digite a string: ")

contador = {}

for letra in s:
    if letra in contador:
        contador[letra] += 1
    else:
        contador[letra] = 1

for chave in contador:
    print("%s: %dx" % (chave, contador[chave]))

print(60 * "=")
