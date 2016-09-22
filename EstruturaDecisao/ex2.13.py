# -*- coding: utf-8 -*-

"""
Faça um Programa que leia um número e exiba o dia correspondente da semana.
(1-Domingo, 2- Segunda, etc.), se digitar outro valor deve aparecer valor inválido.
"""

print("======================================================")

diaSemana = int(input("Digite um numero (1 - Segunda, 2 - Terca, 3 - Quarta,\
				4 - Quinta, 5 - Sexta, 6 - Sabado, 7 - Domingo): "))

if diaSemana == 1:
	print("Hoje e Segunda!")
elif diaSemana == 2:
	print("Hoje e Terca!")
elif diaSemana == 3:
	print("Hoje e Quarta!")
elif diaSemana == 4:
	print("Hoje e Quinta!")
elif diaSemana == 5:
	print("Hoje e Sexta!")
elif diaSemana == 6:
	print("Hoje e Sabado!")
elif diaSemana == 7:
	print("Hoje e Domingo!")
else:
	print("Invalido! tente outra vez.")

print("======================================================")
