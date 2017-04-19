# -*- coding: utf-8 -*-

"""
Faça um Programa que leia um vetor de 5 números inteiros, mostre a soma, a
multiplicação e os números.
"""

print("=======================================================")

vetor = []
soma = 0
mult = 1

for i in range(5):
	num = int(input("Digite o %d" % (i + 1) + " numero: "))
	vetor.append(num)
	soma += num
	mult *= num	

print("Voce digitou: ", vetor)
print("Soma dos numeros: ", soma)
print("Multiplicacao dos numeros: ", mult)

print("=======================================================")