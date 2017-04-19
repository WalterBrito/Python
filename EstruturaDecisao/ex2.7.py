# -*- coding: utf-8 -*-

# Faça um Programa que leia três números e mostre o maior e o menor deles.

print("========================================================")

a = int(input("Digite o primeiro numero: "))
b = int(input("Digite o segundo numero: "))
c = int(input("Digite o terceiro numero: "))

if a > b and a > c:
	print("O numero %d e o maior" % a)
elif b > a and b > c:
	print("O numero %d e o maior" % b)
else: 
	print("O numero %d e o maior" % c)


if a < b and a < c:
	print("O numero %d e o menor" % a)
elif b < a and b < c:
	print("O numero %d e o menor" % b)
else: 
	print("O numero %d e o menor" % c)	

print("========================================================")
