# -*- coding: utf-8 -*-

"""
Faça um Programa que leia um vetor A com 10 números inteiros, calcule e mostre
a soma dos quadrados dos elementos do vetor
"""

print("======================================================")

vetorA = []
soma = 0


for i in range(10):
	num = int(input("Numero %d" % (i + 1) + ": "))
	vetorA.append(num)
	soma +=  num ** 2

print("Numeros do Vetor A: ", vetorA)
print("A soma dos quadrados dos elementos: ", soma)

print("======================================================")