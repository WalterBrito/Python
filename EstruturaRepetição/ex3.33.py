# -*- coding: utf-8 -*-

"""
Uma academia deseja fazer um senso entre seus clientes para descobrir o mais
alto, o mais baixo, a mais gordo e o mais magro, para isto você deve fazer um
programa que pergunte a cada um dos clientes da academia seu código, sua altura
e seu peso. O final da digitação de dados deve ser dada quando o usuário digitar 0
(zero) no campo código. Ao encerrar o programa também deve ser informados os
códigos e valores do cliente mais alto, do mais baixo, do mais gordo e do mais
magro, além da média das alturas e dos pesos dos clientes
"""

print("========================================================")

altura = float(input("Digite sua altura (ex. 1.70): "))
peso = int(input("Digite seu peso (ex. 45): "))
codigo = int(input("Digite seu codigo: "))
sair = int(input("Digite (1) continuar ou (0) sair: "))

maiorAltura = altura
maiorAlturaCodigo = codigo
menorAltura = altura
menorAlturaCodigo = codigo
maiorPeso = peso
maiorPesoCodigo = codigo
menorPeso = peso
menorPesoCodigo = codigo
somaAltura = altura
somaPeso = peso
i = 0

while sair != 0:
	altura = float(input("Digite sua altura (ex. 1.70): "))
	peso = int(input("Digite seu peso (ex. 45): "))
	codigo = int(input("Digite seu codigo: "))
	sair = int(input("Digite (1) continuar ou (0) sair: "))	

	if altura > maiorAltura:
		maiorAltura = altura
		maiorAlturaCodigo = codigo 
	else:
		maiorAltura = maiorAltura

	if altura < menorAltura:
		menorAltura = altura
		menorAlturaCodigo = codigo
	else:
		menorAltura =  menorAltura

	if peso > maiorPeso:
		maiorPeso = peso
		maiorPesoCodigo = codigo
	else:
		maiorPeso = maiorPeso

	if peso < menorPeso:
		menorPeso = peso
		menorPesoCodigo = codigo
	else:
		menorPeso = menorPeso

	somaAltura += altura
	somaPeso += peso
	i += 1

if i != 0:
	mediaPeso = float(somaPeso) / (i + 1)
	mediaAltura = float(somaAltura) / (i + 1)
	print("O mais magro pesa %d Kg codigo %d" % (menorPeso, menorPesoCodigo))
	print("O mais gordo pesa %d kg codigo %d" % (maiorPeso, maiorPesoCodigo))
	print("Tamanho do mais baixo %.2f codigo %d" % (menorAltura, menorAlturaCodigo))
	print("Tamanho do mais alto %.2f codigo %d" % (maiorAltura, maiorAlturaCodigo))
	print("Media Peso: %d Kg" % mediaPeso)
	print("Media altura: %.2f metros" % mediaAltura)

print("========================================================")
