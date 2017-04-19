# -*- coding: utf-8 -*-

"""
Escreva um programa que leia uma string e imprima quantas vezes
cada caractere aparece nessa string.

String: TTAAC

Resultado:

T: 2x
A: 2x
C: 1x
"""

print("=========================================================")

a = input("Digite uma palavra: ")

contador = {}

for letra in a:
	if letra in contador:
		contador[letra]+=1
	else:
		contador[letra]=1

for chave in contador:
	print("%s: %dx" % (chave, contador[chave]))

print("=========================================================")