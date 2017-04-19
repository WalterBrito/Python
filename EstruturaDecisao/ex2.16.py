# -*- coding: utf-8 -*-

"""
Faça um Programa que peça os 3 lados de um triângulo. O programa deverá
informar se os valores podem ser um triângulo. Indique, caso os lados formem um
triângulo, se o mesmo é: equilátero, isósceles ou escaleno.
Dicas:
a. Três lados formam um triângulo quando a soma de quaisquer dois
lados for maior que o terceiro;
b. Triângulo Equilátero: três lados iguais;
c. Triângulo Isósceles: quaisquer dois lados iguais;
d. Triângulo Escaleno: três lados diferentes;
"""

print("======================================================")

lado1 = int(input("Digite o primeiro numero: "))
lado2 = int(input("Digite o segundo numero: "))
lado3 = int(input("Digite o terceiro numero: "))


if lado1 + lado2 > lado3:
	if lado1 == lado2 and lado1 == lado3:
		print("Triangulo Equilatero")
	elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
		print("Triangulo Isosceles")
	elif lado1 != lado2 and lado3 != lado2 or lado3 != lado1:
		print("Triangulo Escaleno")
else:
	print("os lados nao formam um Triangulo.")


print("======================================================")
