# -*- coding: utf-8 -*-

"""
Faça um Programa que leia tres vetores com 10 elementos cada. Gere um quarto
vetor de 30 elementos, cujos valores deverão ser compostos pelos elementos
intercalados dos tres outros vetores.

Obs: Altere o programa anterior, intercalando 3 vetores de 10 elementos cada.
(Essa e a questao, so foi alterado os dados da questao anterior. )
"""

print("========================================================")

vetor1 = []
vetor2 = []
vetor3 = []
vetor4 = []

print("Numeros Vetor 1")
for i in range(10):
	v1 = int(input("Numero %d" % (i + 1) + ": "))
	vetor1.append(v1)
	vetor4.append(v1)
	
print("\nNumeros Vetor 2")
for i in range(10):
	v2 = int(input("Numero %d" % (i + 1) + ": "))
	vetor2.append(v2)
	vetor4.append(v2)

print("\nNumeros Vetor 3")
for i in range(10):
	v3 = int(input("Numero %d" % (i + 1) + ": "))
	vetor3.append(v3)
	vetor4.append(v3)
	
print("Vetor 1: ", vetor1)
print("Vetor 2: ", vetor2)
print("Vetor 3: ", vetor3)
print("Vetor 4: ", (vetor1 + vetor2 + vetor3))

print("========================================================")