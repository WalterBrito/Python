# -*- coding: utf-8 -*-

# Faça um Programa que leia três números e mostre-os em ordem decrescente.

print("========================================================")

a = int(input("Digite o primeiro numero: "))
b = int(input("Digite o segundo numero: "))
c = int(input("Digite o terceiro numero: "))

if a > b and a > c: 
	print("Ordem decrescente: %d %d %d" % (a, c, b))     
elif b > c and b > a: 
	print("Ordem decrescente: %d %d %d" % (b, c, a))                 
else:
	print("Ordem decrescente: %d %d %d" % (c, b, a))                


print("========================================================")
