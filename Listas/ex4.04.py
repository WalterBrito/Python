# -*- coding: utf-8 -*-

"""
Faça um Programa que leia um vetor de 10 caracteres, e diga quantas consoantes
foram lidas. Imprima as consoantes.
"""

print("========================================================")

consoantes = []
vogais = 'aeiou'

for i in range(10):
	consoantes.append(input("Digite uma letra: "))
count = 0

for c in consoantes:
	if c.lower() not in vogais:
		print(c)
		count += 1
print("\nConsoantes: %s" % count)

print("========================================================")