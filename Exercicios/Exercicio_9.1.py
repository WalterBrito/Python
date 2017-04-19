# -*- coding: utf-8 -*-

"""
Escreva um programa que receba o nome de um arquivo pela linha
de comando e que imprima todas as linhas desse arquivo.
"""

print(60 * "=")

import sys

if (len(sys.argv) != 2):
	print("\nPython\n\n")
else:
	nome = sys.argv[1]
	arquivo = open(nome, "r")

	for linha in arquivo.readlines():
		print(linha[:-1])

	arquivo.close()


# nome = input("Digite um nome: ")
# arquivo = open(nome, "w")

# for linha in range(10):
# 	arquivo.write("%d\n" % linha)
# 	print(linha)

# arquivo.close()


print(60 * "=")