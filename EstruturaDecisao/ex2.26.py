# -*- coding: utf-8 -*-

"""
Faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As
perguntas são:
a."Telefonou para a vítima?"
b."Esteve no local do crime?"
c."Mora perto da vítima?"
d."Devia para a vítima?"
e."Já trabalhou com a vítima?"
O programa deve no final emitir uma classificação sobre a participação da
pessoa no crime. Se a pessoa responder positivamente a 2 questões ela deve ser
classificada como "Suspeita", entre 3 e 4 como "Cúmplice" e 5 como "Assassino".
Caso contrário, ele será classificado como "Inocente".
"""

print("=========================================================")

pergunta1 = input("Telefonou para a vítima? (S ou N): ")
if pergunta1 == "S" or pergunta1 == "s":	
	pergunta1 = 1
else:
	pergunta1 = 0

pergunta2 = input("Esteve no local do crime? (S ou N): ")
if pergunta2 == "S" or pergunta2 == "s":	
	pergunta2 = 1
else:
	pergunta2 = 0

pergunta3 = input("Mora perto da vítima? (S ou N): ")
if pergunta3 == "S" or pergunta3 == "s":	
	pergunta3 = 1
else:
	pergunta3 = 0

pergunta4 = input("Devia para a vítima? (S ou N): ")
if pergunta4 == "S" or pergunta4 == "s":	
	pergunta4 = 1
else:
	pergunta4 = 0

pergunta5 = input("Já trabalhou com a vítima? (S ou N): ")
if pergunta5 == "S" or pergunta5 == "s":	
	pergunta5 = 1
else:
	pergunta5 = 0

respostas = pergunta1+pergunta2+pergunta3+pergunta4+pergunta5

if respostas <= 1:
	print("Voce e Inocente!")
elif respostas <=  2:
	print("Voce e Suspeito(a)!")
elif respostas > 2 and respostas <= 4:
	print("Voce e Cumplice!")
elif respostas == 5:
	print("Voce e o Assassino(a)!")
else:
	print("Resposta invalida! tente outra vez.")


print("=========================================================")
