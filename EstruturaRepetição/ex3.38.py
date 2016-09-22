# -*- coding: utf-8 -*-

"""
Faça um programa que leia uma quantidade indeterminada de números positivos e
conte quantos deles estão nos seguintes intervalos: [0-25], [26-50], [51-75] e [76-
100]. A entrada de dados deverá terminar quando for lido um número negativo.
"""

print("=======================================================")

num = 0
entre0e25 = 0
entre26e50 = 0
entre51e75 = 0
entre76e100 = 0

i = 0
while num >= 0:
	num = int(input("Digite um numero positivo (para sair digite um numero negativo): "))

	if 0 <= num <= 25:
		entre0e25 += 1
	elif 26 <= num <= 50:
		entre26e50 += 1
	elif 51 <=  num <= 75:
		entre51e75 += 1
	elif 76 <= num <= 100:
		entre76e100 += 1

print("Numeros no intervalo [0-25]: %d" % entre0e25)
print("Numeros no intervalo [26-50]: %d" % entre26e50)
print("Numeros no intervalo [51-75]: %d" % entre51e75)
print("Numeros no intervalo [76-100]: %d" % entre76e100)

print("=======================================================")






