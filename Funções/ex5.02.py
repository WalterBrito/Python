# -*- coding: utf-8 -*-

"""
Faça um programa, com uma função que necessite de três argumentos, e que
forneça a soma desses três argumentos.
"""

print("======================================================")

def soma(soma1, soma2, soma3):
	return soma1 + soma2 + soma3

numeros = []

i = 0
for i in range(3):
	numero = int(input("Digite o numero %d" % (i+1) + ": "))
	numeros.append(numero)
	i += 1

print("A soma dos numeros: ", soma(numeros[0], numeros[1], numeros[2]))

print("======================================================")