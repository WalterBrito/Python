# -*- coding: utf-8 -*-

# Faça um Programa que peça dois números e imprima o maior deles.

print("======================================================")

a = int(input("Digite o primeiro numero (a): "))
b = int(input("Digite o primeiro numero (b): "))

if a > b:
	print("%d e maior que %d." % (a, b))
else:
	print("%d e maior que %d." % (b, a))

print("======================================================")
