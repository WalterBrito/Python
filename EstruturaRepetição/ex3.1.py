# -*- coding: utf-8 -*-

"""
Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem
caso o valor seja inválido e continue pedindo até que o usuário informe um valor
válido.
"""


print("=======================================================")

while True:
	nota = int(input("Digite uma nota (0 a 10): "))

	if nota <= 10:
		print("A nota e %d." % nota)
		break
	else:
		print("Valor invalido! tente outra vez.")



print("=======================================================")
