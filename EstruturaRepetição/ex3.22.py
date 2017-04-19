# -*- coding: utf-8 -*-

"""
Numa eleição existem três candidatos. Faça um programa que peça o número total
de eleitores. Peça para cada eleitor votar e ao final mostrar o número de votos de
cada candidato.
"""

print("===============================================================")

n = int(input("Digite o numero de eleitores: "))

i = 0
soma1 = 0
soma2 = 0
soma3 = 0

while i < n:
	voto = int(input("Digite (1) Candidato 1, (2) Candidato 2, (3) Candidato 3: "))
	if voto == 1:
		soma1 += 1
	elif voto == 2:
		soma2 += 1
	elif voto == 3:
		soma3 += 1
	i += 1

print("Numero de votos Candidato 1: %d" % soma1)
print("Numero de votos Candidato 2: %d" % soma2)
print("Numero de votos Candidato 3: %d" % soma3)

print("===============================================================")
