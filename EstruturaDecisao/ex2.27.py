# -*- coding: utf-8 -*-

"""
Um posto está vendendo combustíveis com a seguinte tabela de
descontos:
a. Álcool:
b. até 20 litros, desconto de 3%  por litro
c. acima de 20 litros, desconto de 5%  por litro
d. Gasolina:
e. até 20 litros, desconto de 4%  por litro
f. acima de 20 litros, desconto de 6%  por litro
Escreva um algoritmo que leia o número de litros vendidos, o tipo de
combustível (codificado da seguinte forma: A-álcool, G-gasolina), calcule e
imprima o valor a ser pago pelo cliente sabendo-se que o preço do litro da
gasolina é R$ 2,50 o preço do litro do álcool é R$ 1,90.
"""

print("=========================================================")

quantLitros = float(input("Quantos litros voce deseja:  "))
combustivel = input("Voce deseja Alcool ou Gasolina?: ")

if combustivel == "A" or combustivel == "a":
		if quantLitros <= 20:
			descAlcool = (quantLitros * 1.9) * (1 - 0.03)
			print("O tipo de combustivel e Alcool.")
			print("O total a pagar: %.2f" % descAlcool)
		elif quantLitros > 20:
			descAlcool = (quantLitros * 1.9) * (1 - 0.05)
			print("O tipo de combustivel e Alcool.")
			print("O total a pagar: %.2f" % descAlcool)

if combustivel == "G" or combustivel == "g":
		if quantLitros <= 20:
			descGasolina = (quantLitros * 2.5) * (1 - 0.04)
			print("O tipo de combustivel e Gasolina.")
			print("O total a pagar: %.2f" % descGasolina)
		elif quantLitros > 20:
			descGasolina = (quantLitros * 2.5) * (1 - 0.06)
			print("O tipo de combustivel Gasolina.")
			print("O total a pagar: %.2f" % descGasolina)


print("=========================================================")
