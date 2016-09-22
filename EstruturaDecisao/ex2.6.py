# -*- coding: utf-8 -*-

# Faça um Programa que leia três números e mostre o maior deles.

print("========================================================")

a = int(input("Digite o primeiro numero: "))
b = int(input("Digite o segundo numero: "))
c = int(input("Digite o terceiro numero: "))

if a > b and  a > c:
	print("%d e o maior." % a)
elif b > a  and b > c:
	print("%d e o maior." % b)
else:
	print("%d e o maior." % c)

print("========================================================")
