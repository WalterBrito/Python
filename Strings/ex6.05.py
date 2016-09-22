# -*- coding: utf-8 -*-

"""
'''Nome na vertical em escada invertida.''' Altere o programa anterior de modo que
a escada seja invertida.
FULANO
FULAN
FULA
FUL
FU
F
"""

print("=======================================================")

nome = input("Digite seu nome: ").capitalize()

i = len(nome)
while i > 0:
	print(nome[0:i])
	i -= 1

print("=======================================================")