# -*- coding: UTF-8 -*-

'''
Tendo como dados de entrada a altura e o sexo de uma pessoa, construa um
algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
a. Para homens: (72.7*h) - 58
b. Para mulheres: (62.1*h) - 44.7 (h = altura)
c. Peça o peso da pessoa e informe se ela está dentro, acima ou abaixo do
peso.
'''

print("======================================================")

print("Na altura use ponto nao virgula")
h = float(input("Digite sua altura (ex: 1.70): "))
sexo = int(input("Digite seu sexo (1) homem (2)mulher: "))
peso = int(input("Digite seu peso: "))

pesoHomem = ((72.7*h) - 58)
pesoMulher = ((62.1*h) - 44.7)

if sexo == 1:
	print("Seu peso ideal e: %.1f" % pesoHomem)
elif peso > pesoHomem:
	print("Voce esta acima do seu peso ideal.")
elif peso == pesoHomem:
	print("Voce esta no peso ideal.")
elif peso < pesoHomem:
	print("Voce esta abaixo do seu peso ideal.")
if sexo == 2:
	print("Seu peso ideal e: %.1f" % pesoMulher)
elif peso > pesoMulher:
	print("Voce esta acima do seu peso ideal.")
elif peso == pesoMulher:
	print("Voce esta no peso ideal.")
elif peso < pesoMulher:
	print("Voce esta abaixo do seu peso ideal.")

print("======================================================")
