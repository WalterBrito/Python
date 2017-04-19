# -*- coding: utf-8 -*-

"""
Faça um programa que peça dois números, base e expoente, calcule e mostre o
primeiro número elevado ao segundo número. Não utilize a função de potência da
linguagem
"""

print("===============================================================")

num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))

while True:
	if (num1 and num2) > 0:
		print("O primeiro elavado ao segundo: %d" % (num1 ** num2))
		break
		
print("===============================================================")
