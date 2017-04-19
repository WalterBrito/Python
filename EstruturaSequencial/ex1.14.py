# -*- coding: utf-8 -*-

"""
João Papo-de-Pescador, homem de bem, comprou um microcomputador para
controlar o rendimento diário de seu trabalho. Toda vez que ele traz um peso de
peixes maior que o estabelecido pelo regulamento de pesca do estado de São
Paulo (50 quilos) deve pagar uma multa de R$ 4,00 por quilo excedente. João
precisa que você faça um programa que leia a variável peso (peso de peixes) e
verifique se há excesso. Se houver, gravar na variável excesso e na variável multa
o valor da multa que João deverá pagar. Caso contrário mostrar tais variáveis com
o conteúdo ZERO.
"""

print("=====================================================")

pesoPeixe = 50
multa = 4
excesso = 0
quant = int(input("Digite a quantidade de peixes (Kg): "))

if quant > pesoPeixe:
	excesso = quant - pesoPeixe
	multa = excesso * multa
	print("Voce tem %d kg de peixes." % quant)
	print("Voce ultrapassou o limite do regulamento.")
	print("A valor da multa e: R$ %.2f reais." % multa)
else:
	print("Voce tem %d kg de peixes." % quant)
	print("Voce esta dentro do limite permitido.")
	print("Voce esta isento da multa.")

print("=====================================================")
