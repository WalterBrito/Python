# -*- coding: utf-8 -*-

"""
Escreva um programa que leia duas strings e gere uma terceira,
na qual os caracteres da segunda foram retirados da terceira.
1° string: AATTGGAA
2° string: TG
3° string: AAAA
"""

print("==========================================================")

a = input("Digite o primeiro nome: ")
b = input("Digite o segundo nome: ")
c = ""

for letra in a:
	if letra not in b:
		c += letra

if c == "":
	print("Todos os caracteres foram removidos.")
else:
	print("Os caracteres %s foram removidos de %s." % (b, a))
	print("3° string: %s" % c)

print("==========================================================")