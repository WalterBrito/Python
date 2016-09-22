# -*- coding: utf-8 -*-

"""
Faça uma função que informe a quantidade de dígitos de um determinado número
inteiro informado.
"""

print("=======================================================")

def quantDigitos(numero):
	numeroStr = str(numero)
	return len(numeroStr)

i = 0
while i == 0:
	numero = int(input("Digite um numero: "))
	print("Quantidade de numeros digitados: ", quantDigitos(numero))
	i = int(input("\nDigite 0 para continuar ou 1 paa sair: "))
	if i == 1:
		print("\nAte a proxima!\n\n")

print("=======================================================")