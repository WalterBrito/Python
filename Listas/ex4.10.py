# -*- coding: utf-8 -*-

"""
Faça um Programa que leia dois vetores com 10 elementos cada. Gere um terceiro
vetor de 20 elementos, cujos valores deverão ser compostos pelos elementos
intercalados dos dois outros vetores.
"""

print("========================================================")

vetor1 = []
vetor2 = []
vetor3 = []

print("Numeros Vetor 1")
for i in range(10):
	v1 = int(input("Numero %d" % (i + 1) + ": "))
	vetor1.append(v1)
	vetor3.append(v1)
	

print("\nNumeros Vetor 2")
for i in range(10):
	v2 = int(input("Numero %d" % (i + 1) + ": "))
	vetor2.append(v2)
	vetor3.append(v2)
	

print("Vetor 1: ", vetor1)
print("Vetor 2: ", vetor2)
print("Vetor 3: ", (vetor1 + vetor2))

print("========================================================")