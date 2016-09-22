# -*- coding: utf-8 -*-

"""
Faça um Programa para um caixa eletrônico. O programa deverá perguntar ao
usuário a valor do saque e depois informar quantas notas de cada valor serão
fornecidas. As notas disponíveis serão as de 1, 5, 10, 50 e 100 reais. O valor
mínimo é de 10 reais e o máximo de 600 reais. O programa não deve se preocupar
com a quantidade de notas existentes na máquina.
a. Exemplo 1: Para sacar a quantia de 256 reais, o programa fornece
duas notas de 100, uma nota de 50, uma nota de 5 e uma nota de 1;
b. Exemplo 2: Para sacar a quantia de 399 reais, o programa fornece
três notas de 100, uma nota de 50, quatro notas de 10, uma nota de 5 e
quatro notas de 1.
"""

print("=========================================================")

valorSaque = int(input("Qual o valor do saque R$: "))

numStr = str(valorSaque)
quantNum = len(numStr)
nota100  = "nota(s) de cem"
nota50   = "nota(s) de cinquenta"
nota10   = "nota(s) de dez"
nota5    = "nota(s) de cinco"
nota1    = "nota(s) de um"

if quantNum == 3:
	centena = int(numStr[0:1]) 
	dezena = int(numStr[1:2]) 
	unidade = int(numStr[0:1]) 
	print(centena, nota100)
	if 0 < dezena < 5:
		print(dezena, nota10)
	if dezena == 5:
		print("1", nota50)
	if dezena > 5:
		print("1", nota50)
		print((dezena - 5), nota10) 
	if 0 < unidade < 5:
		print(unidade, nota1)
	if unidade == 5:
		print(unidade, nota5)
	if unidade > 5:
		print("1", nota5)
		print((unidade - 5), nota1)

if quantNum == 1:
	dezena = int(numStr[0:1]) 
	unidade = int(numStr[1:2]) 	
	if 0 < dezena < 5:
		print(dezena, nota10)
	if dezena == 5:
		print("1", nota50)
	if dezena > 5:
		print("1", nota50)
		print((dezena - 5), nota10) 
	if 0 < unidade < 5:
		print(unidade, nota1)
	if unidade == 5:
		print(unidade, nota5)
	if unidade > 5:
		print("1", nota5)
		print((unidade - 5), nota1)

if quantNum == 1:
	unidade = int(numStr[0:1]) 
	if 0 < dezena < 5:
		print(dezena, nota10)
	if 0 < unidade < 5:
		print(unidade, nota1)
	if unidade == 5:
		print(unidade, nota5)
	if unidade > 5:
		print("1", nota5)
		print((unidade - 5), nota1)



print("=========================================================")
