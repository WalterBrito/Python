# -*- coding: utf-8 -*-

"""
Faça um programa que calcule o fatorial de um número inteiro fornecido pelo
usuário. Ex.: 5!=5.4.3.2.1=120. A saída deve ser conforme o exemplo abaixo:
Fatorial de: 5
5! = 5 . 4 . 3 . 2 . 1 = 120
"""

print("===============================================================")

num = int(input("Digite um numero: "))
numCalc = num
fatorial = 1
print("Fatorial de: %d" % num)
while numCalc > 0:
	fatorial *= numCalc
	if numCalc > 1:
		print("%d . %d" % (num, numCalc))
	else:
		print("  . %d" % numCalc)
	numCalc -= 1

print("Resultado Fatorial de %d = %d " % (num, fatorial)) 

print("===============================================================")
