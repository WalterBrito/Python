# -*- coding: utf-8 -*-

"""
Faça um programa que lê as duas notas parciais obtidas por um aluno numa
disciplina ao longo de um semestre, e calcule a sua média. A atribuição de
conceitos obedece à tabela abaixo:
Média   de Aproveitamento Conceito
Entre	9.0 e 10.0			A
Entre	7.5 e 9.0			B
Entre	6.0 e 7.5			C
Entre	4.0 e 6.0			D
Entre	4.0 e zero			E
"""

print("======================================================")


nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 9 and media <= 10:
	print("Conceito A")
elif media >= 7.5 and media < 9:
	print("Conceito B")
elif media >= 6 and media < 7.5:
	print("Conceito C")
elif media >= 4 and media < 6:
	print("Conceito D")
elif media < 4 and media >= 0:
	print("Conceito E")

print("Media: %.1f" % media)

print("======================================================")
