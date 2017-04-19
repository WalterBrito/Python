# -*- coding: utf-8 -*-

"""
O Departamento Estadual de Meteorologia lhe contratou para desenvolver um
programa que leia as um conjunto indeterminado de temperaturas, e informe ao
final a menor e a maior temperaturas informadas, bem como a média das
temperaturas.
"""

print("=================================================================")

i = 0
soma = 0
a = 0

temperatura = input("Digite uma temperatura ou s para sair: ")
maiorTemperatura = temperatura
menorTemperatura = temperatura

if temperatura == "s":
	maiorTemperatura == maiorTemperatura
	a = temperatura
else:
	temperatura = float(temperatura)

while a != "s":
	if temperatura > maiorTemperatura:
		maiorTemperatura = temperatura
	else:
		temperatura = temperatura
	if temperatura < menorTemperatura:
		menorTemperatura = temperatura
	else:
		menorTemperatura = menorTemperatura

	soma += temperatura
	temperatura = input("Digite uma temperatura ou s para sair: ")
	if temperatura == "s":
		temperatura = temperatura
		a = temperatura
	else:
		temperatura = float(temperatura)
		i += 1	

if i > 0:
	media = soma / i
	print("Maior Temperatura: %.2f graus." % maiorTemperatura)
	print("Menor Temperatura: %.2f graus." % menorTemperatura)
	print("Soma das temperaturas = %.2d graus" % soma)
	print("Media das temperaturas: %.2f" % media)

print("=================================================================")
