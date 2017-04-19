# -*- coding: utf-8 -*-

"""
'''Reverso do número.''' Faça uma função que retorne o reverso de um número
inteiro informado. Por exemplo: 127 -> 721.
"""

print("======================================================")

def reverso(numero):
	numeroStr = str(numero)
	i = len(numeroStr)
	numeroInvertStr = ""
	while i > 0:
		numeroInvertStr = numeroInvertStr + numeroStr[i-1:i]
		i -= 1
	numeroInvert = int(numeroInvertStr)
	return numeroInvert

i = 0
while i == 0:
	numero = int(input("Digite um numero: "))
	print("O numero digitado %d e o reverso e %d." % (numero, reverso(numero))) 
	i = int(input("\nDigite 0 para continuar ou 1 para sair: "))
	if i == 1:
		print("\nAte a proxima!\n\n")

print("======================================================")