# -*- coding: utf-8 -*-

# Faça um Programa que leia 4 notas, mostre as notas e a média na tela.

print("======================================================")

notas = []
media = 0

for i in range(4):
	notas.append(float(input("Digite a nota " + str(i + 1)+ ": ")))
for i in range(len(notas)):
	media += notas[i]
media /= len(notas)
print("Media: %.1f" % media)

print("======================================================")