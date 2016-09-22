# -*- coding: utf-8 -*-

"""
Faça um programa que pergunte o preço de três produtos e informe qual produto
você deve comprar, sabendo que a decisão é sempre pelo mais barato.
"""

print("========================================================")

produto1 = float(input("Digite o preco do produto (1): "))
produto2 = float(input("Digite o preco do produto (2): "))
produto3 = float(input("Digite o preco do produto (3): "))

if produto1 < produto2 and produto1 < produto3:
	print("O produto com valor R$ %.2f e o mais barato." % produto1)
elif produto2 < produto1 and produto2 < produto3:
	print("O produto com valor R$ %.2f e o mais barato." % produto2)
else:
	print("O produto com valor R$ %.2f e o mais barato." % produto3)


print("========================================================")
