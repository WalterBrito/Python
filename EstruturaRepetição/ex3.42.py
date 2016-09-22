# -*- coding: utf-8 -*-

"""
Faça um programa que peça um numero inteiro positivo e em seguida mostre este
numero invertido.
Exemplo:
12376489
=> 98467321
"""

print("======================================================")

num = int(input("Digite um numero inteiro positivo: "))
numStr = str(num)
i = len(numStr)

while i >= 0:
	print(numStr [i - 1: i]),
	i -= 1

print("\n=======================================================")
