# -*- coding: utf-8 -*-

"""
Escreva uma programa que leia duas strings e gere uma terceira com os 
caracteres que aparecem em apenas uma delas.
1° string: CTA
2° string: ABC
3° string: BT
A ordem dos caracteres da 3° string nao e importante.
"""

print("==========================================================")

a = input("Digite o primeiro nome: ")
b = input("Digite o primeiro nome: ")
c = ""

for letra in a:
	if letra not in b and letra not in c:
		c += letra

for letra in b:
	if letra not in a and letra not in c:
		c += letra

if c == "":
	print("Caracteres incomuns nao encontrados.")
else:
	print("Caracteres incomuns: %s" % c)

print("==========================================================")