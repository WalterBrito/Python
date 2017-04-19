# -*- coding: utf-8 -*-

"""
'''Nome na vertical em escada.''' Modifique o programa anterior de forma a
mostrar o nome em formato de escada.
"""

print("=========================================================")

nome = input("Digite seu nome: ").capitalize()

i = 1
while i < len(nome) + 1:
	print(nome[0:i])
	i += 1

print("=========================================================")