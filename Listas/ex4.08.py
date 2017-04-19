# -*- coding: utf-8 -*-

"""
Faça um Programa que peça a idade e a altura de 5 pessoas, armazene cada
informação no seu respectivo vetor. Imprima a idade e a altura na ordem inversa a
ordem lida.
"""

print("=======================================================")

idade = []
altura = []

for i in range(5):
	print("Pessoa %d" % (i + 1))
	for y in range(1):
		a = int(input("Digite sua idade: "))
		b = float(input("Digite sua altura: "))
	idade.append(a)
	altura.append(b)
	i += 1

idade.reverse()
print("Idade ",  idade)
altura.reverse()
print("Altura", altura)	

print("=======================================================")