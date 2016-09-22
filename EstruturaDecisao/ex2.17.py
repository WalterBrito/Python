# -*- coding: utf-8 -*-

"""
Faça um programa que calcule as raízes de uma equação do segundo grau, na
forma ax2 + bx + c. O programa deverá pedir os valores de a, b e c e fazer as
consistências, informando ao usuário nas seguintes situações:
a. Se o usuário informar o valor de A igual a zero, a equação não é
do segundo grau e o programa não deve pedir os demais valores,
sendo encerrado;
b. Se o delta calculado for negativo, a equação não possui raizes
reais. Informe ao usuário e encerre o programa;
c. Se o delta calculado for igual a zero a equação possui apenas uma
raiz real; informe-a ao usuário;
d. Se o delta for positivo, a equação possui duas raizes reais;
informe-as ao usuário;
"""

print("=====================================================")

import math

a = int(input("Digite o primeiro numero: "))
if a == 0:
	print("A equação nao e do segundo grau.")
else:
	b = int(input("Digite o segundo numero: "))
	c = int(input("Digite o terceiro numero: "))
	delta = (math.pow(b,2) - (4*a*c))
	if delta < 0:
		print("A equacao nao possui raizes reais.")
	if delta == 0:
		raiz = ((-1) * b + math.sqrt(delta) / (2 * a))
		print("A equacao possui apenas uma raiz real. %.2f" % raiz)
	if delta > 0:
		raiz1 = ((-1) * b + math.sqrt(delta) / (2 * a))
		raiz2 = ((-1) * b - math.sqrt(delta) / (2 * a))
		print("A equacao possui duas raizes reais.")
		print("Raiz 1: %.2f" % raiz1)
		print("Raiz 2: %.2f" % raiz2)

print("=====================================================")
