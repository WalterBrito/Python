# -*- coding: utf-8 -*-

"""
Impressão de números impares de 1 até o número
digitado pelo usuário.
"""

print(60 * "=")

fim = int(input("Digite o último número: "))

x = 1
while x <= fim:
	print(x)
	x += 2

print(60 * "=")
