# -*- coding: utf-8 -*-

"""
Modifique o programa anterior para que receba mais dois 
parâmetros a linha de inicio e de fim para impressão. O
programa deve imprimir apenas as linhas entre esses dois 
valores incluindo as linhas de inicio e fim.
"""

print(60 * "=")

import sys

if (len(sys.argv) != 2):
	print("\nPython inicio fim\n\n")
else:
	nome = sys.argv[1]
	inicio = int(sys.argv[2])
	fim = int(sys.argv[3])
	arquivo = open(nome, "r")

	for linha in arquivo.readlines():
		print(linha[:-1])

	arquivo.close()


print(60 * "=")