# -*- coding: utf-8 -*-

"""
Modifique o programa anterior de forma a ler um número n.
Imprima os n primeiros números primos.
"""

print(60 * "=")

num = int(input("Digite um número: ")) 
if num < 0:
	print('Número inválido. Digite apenas valores positivos.')
else:
	if num >= 1:
		print("2")
		primo = 1
		y = 3

		while primo < num:
			x = 3

			while (x < y):
				if y % x == 0:
					break
				x += 2
			if x == y:
				print(x)
				primo += 1
			y += 2

print(60 * "=")