# -*- coding: utf-8 -*-

"""
Faça um Programa que peça um número correspondente a um determinado ano e
em seguida informe se este ano é ou não bissexto.
"""

print("=========================================================")

anoBi = int(input("Digite um ano (ex. 2015): "))

if (anoBi % 4 == 0) or (anoBi % 400 == 0) and (anoBi % 100 != 0):
	print("O ano e Bissexto!")
else:
	print("O ano nao e Bissexto!")


print("=========================================================")
