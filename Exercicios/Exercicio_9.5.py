# -*- coding: utf-8 -*-

"""
Crie um programa que inverta a ordem das linhas do arquivo 
pares.txt. A primeira linha deve conter o maior número: e a ultima,
o menor.
"""

print(60 * "=")

pares = open("pares.txt", "r")
saida = open("paresInvertidos.txt", "w")

l = pares.readlines()
l.reverse()

for linha in l:
	saida.write(linha)

pares.close()
saida.close()


print(60 * "=")

