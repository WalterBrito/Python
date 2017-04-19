# -*- coding: utf-8 -*-

"""
''Nome ao contrário em maiúsculas.''' Faça um programa que permita ao usuário
digitar o seu nome e em seguida mostre o nome do usuário de trás para frente
utilizando somente letras maiúsculas. Dica: lembre−se que ao informar o nome o
usuário pode digitar letras maiúsculas ou minúsculas.
"""

print("==========================================================")

nome = input("Digite seu nome: ")
nomeInvertido = ""
i = len(nome) - 1
while i >= 0:
	nomeInvertido += nome[i: i+1]
	i -= 1 
	print("Nome de tras pra frente %s." % nomeInvertido.upper())

print("==========================================================")