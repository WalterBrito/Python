# -*- coding: utf-8 -*-

"""
Faça um Programa que peça um número e informe se o número é inteiro ou
decimal. Dica: utilize uma função de arredondamento.
"""

print("=========================================================")

num = input("Digite um numero: ")

if round(num) == num:	
	print("O numero %d e inteiro!" % num)
else:
	print("O numero %.1f e decimal." % num)


print("=========================================================")
