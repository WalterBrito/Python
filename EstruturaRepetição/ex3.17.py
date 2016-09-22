# -*- coding: utf-8 -*-

"""
Faça um programa que peça um número inteiro e determine se ele é ou não um
número primo. Um número primo é aquele que é divisível somente por ele mesmo
e por 1.
"""

print("===============================================================")

num = int(input("Digite um numero: "))
i = 2

while i < num:
	if num % i == 0:
		a = 0
		i = num
	else:
		i += 1
		a = 1
if a == 1 or num == 2:
	print("Numero %d e primo!" % num)
else:
	print("Numero %d nao e primo!" % num)
	

print("===============================================================")

