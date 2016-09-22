# -*- coding: utf-8 -*-

"""
'''Embaralha palavra'''. Construa uma função que receba uma string como
parâmetro e devolva outra string com os carateres embaralhados. Por exemplo: se
função receber a palavra ''python'', pode retornar ''npthyo'', ''ophtyn'' ou qualquer
outra combinação possível, de forma aleatória. Padronize em sua função que
todos os caracteres serão devolvidos em caixa alta ou caixa baixa,
independentemente de como foram digitados.
"""

print("=======================================================")

import random

def embaralha(palavra):
	n = len(palavra)
	i = 0
	letras = []
	while i < len(palavra):
		letras.append(palavra[i:i+1])
		i += 1

	indiceSort = range(len(letras))

	resultList = []
	i = 0
	while len(indiceSort) > 0:
		indice = random.choice(indiceSort)
		resultList.append(letras[indice])
		indiceSort.remove(indice)
		i += 1

	resultStr = ""
	i = 0
	while i < len(resultList):
		resultStr = resultStr + resultList[i]
		i += 1
	print(resultStr)

i = 0
while i == 0:
	palavraEntrada = input("Digite uma palavra que sera embaralhada: ")
	print("Palavra embaralhada: ", embaralha(palavraEntrada))
	i = int(input("Digite 0 para continuar ou 1 para sair: "))
	if i == 1:
		print("\nAte a proxima\n\n")

print("=======================================================")