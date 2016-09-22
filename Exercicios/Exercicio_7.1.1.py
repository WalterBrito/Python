# -*- coding: utf-8 -*-

"""
Escreva um programa que leia duas strings. Verifique se a segunda 
ocorre dentro da primeira e imprima a posição de inicio.

1° string: AABBEFAATT
2° string: BE
Resultado: BE encontrado na posição 3 AABBEFAATT
"""

print(60 * "=")

s1 = "Python"
s2 = "Python e Django"

p = 0

while(p > -1):
	p = s2.find("th", p)

	if p >= 0:
		print("s2 dentro de s1!")
		print("Posição: %d" % p)
		p += 1

print(60 * "=")