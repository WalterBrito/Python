# -*- coding: utf-8 -*-

"""
O algoritmo deve mostrar na tela as notas, a média, o conceito correspondente e
a mensagem “APROVADO” se o conceito for A, B ou C ou “REPROVADO” se
o conceito for D ou E."""


print("======================================================")

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media >= 9 and media <= 10:
	print("Conceito A")
	print("APROVADO")
elif media >= 7.5 and media < 9:
	print("Conceito B")
	print("APROVADO")
elif media >= 6 and media < 7.5:
	print("Conceito C")
	print("APROVADO")
elif media >= 4 and media < 6:
	print("Conceito D")
	print("REPROVADO")
elif media < 4 and media >= 0:
	print("Conceito E")
	print("REPROVADO")

print("Media: %.1f" % media)


print("======================================================")
