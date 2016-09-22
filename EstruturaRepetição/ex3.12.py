# -*- coding: utf-8 -*-

"""
Faça um programa que peça 10 números inteiros, calcule e mostre a quantidade de
números pares e a quantidade de números impares.
"""

print("===============================================================")

par = 0
impar = 0

for i in range(10):
	num = int(input("Digite um numero: "))

	if num % 2 == 0:
		par += 1		
	else:
		impar += 1

print("Numeros Pares: %d" % par)
print("Numeros Impares: %d" % impar)


print("===============================================================")
