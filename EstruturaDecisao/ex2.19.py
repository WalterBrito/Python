# -*- coding: utf-8 -*-

"""
Faça um Programa que peça uma data no formato dd/mm/aaaa e determine se a
mesma é uma data válida.
"""


print("=========================================================")

dia = int(input("Digite um dia (ex. 15): "))
mes = int(input("Digite um mes (ex. 12): "))
ano = int(input("Digite um ano (ex. 2015): "))

if (dia > 0 and dia <= 31) and (mes >= 1 and mes <= 12) and ano > 0:
	print("A data %d/%d/%d e valida!" % (dia, mes, ano))
else:
	print("A data %d/%d/%d nao e valida!" % (dia, mes, ano))


print("=========================================================")
