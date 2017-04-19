# -*- coding: utf-8 -*-

"""
Escreva uma programa que leia duas strings e gere uma terceira com os 
caracteres comuns as duas strings lidas.
1° string: AABBEFAATT
2° string: BE
Resultado: BE 
A ordem dos caracteres da string gerada nao e importante, mas deve conter 
todas as letras comuns a ambas. 
"""

print("==========================================================")

a = input("Digite o primeiro nome: ")
b = input("Digite o segundo nome: ")
c = ""

for letra in a:
	if letra in b and letra not in c:
		c += letra

if c == "":
	print("Caracteres comuns nao encontrados.")
else:
	print("Caracteres comuns: %s" % c)

print("==========================================================")