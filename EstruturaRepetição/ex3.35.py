# -*- coding: utf-8 -*-

"""
Faça um programa que leia dez conjuntos de dois valores, o primeiro
representando o número do aluno e o segundo representando a sua altura em
centímetros. Encontre o aluno mais alto e o mais baixo. Mostre o número do
aluno mais alto e o número do aluno mais baixo, junto com suas alturas
"""

print("========================================================")

num = int(input("Digite o numero do aluno: "))
altura = float(input("Digite a altura do aluno: "))
maiorAltura = altura
maiorAlturaNum = num 
menorAltura = altura
menorAlturaNum = num

i = 1 
while i < 3:
	num = int(input("\nDigite o numero do aluno: "))
	altura = float(input("Digite a altura do aluno: "))

	if altura > maiorAltura:
		maiorAltura = altura
		maiorAlturaNum = num

	if altura < menorAltura:
		menorAltura = altura
		menorAlturaNum = num
	i += 1

print("Numero de alunos baixos: %d" % menorAlturaNum)
print("O mais baixo tem %.2f metros." % menorAltura)
print("Numero de alunos altos: %d" % maiorAlturaNum)
print("O mais alto tem %.2f metros." % maiorAltura)

print("========================================================")
