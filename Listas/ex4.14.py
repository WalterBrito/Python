# -*- coding: utf-8 -*-

"""
Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre
um crime. As perguntas são:
a.'Telefonou para a vítima?'
b.'Esteve no local do crime?'
c.'Mora perto da vítima?'
d.'Devia para a vítima?'
e.'Já trabalhou com a vítima?'
O programa deve no final emitir uma classificação sobre a
participação da pessoa no crime. Se a pessoa responder
positivamente a 2 questões ela deve ser classificada como
'Suspeita', entre 3 e 4 como 'Cúmplice' e 5 como 'Assassino'. Caso
contrário, ele será classificado como 'Inocente'.
"""

print("=======================================================")

perguntas = ['Telefonou para a vítima?', 'Esteve no local do crime?',
'Mora perto da vítima?', 'Devia para a vítima?', 'Já trabalhou com a vítima?']

soma = 0
i = 0
for i in range(len(perguntas)):
	resposta = input(perguntas[i] + ": ")
	if resposta == 's':
		soma += 1
	else:
		soma = soma
	i += 1

if soma < 2:
	print("Inocente!")
elif soma == 2:
	print("Suspeito(a)!")
elif soma > 2 and soma <= 4:
	print("Cumplice!")
elif soma == 5:
	print("Assassino(a).")

print("=======================================================")