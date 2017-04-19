# -*- coding: utf-8 -*-

# Faça um programa que calcule o mostre a média aritmética de N notas.

print("===============================================================")

notas = float(input("Digite um numero de notas: "))	

i = 0
soma = 0

while i < notas:
	nota = float(input("Digite uma nota: "))
	soma = soma + nota
	i += 1
media = soma / i
print("Media: %.1f" % media)


print("===============================================================")
