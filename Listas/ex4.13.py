# -*- coding: utf-8 -*-

"""
Faça um programa que receba a temperatura média de cada mês do ano e
armazene-as em uma lista. Após isto, calcule a média anual das temperaturas e
mostre todas as temperaturas acima da média anual, e em que mês elas ocorreram
(mostrar o mês por extenso: 1 – Janeiro, 2 – Fevereiro, . . . ).
"""

print("=========================================================")

meses = ["Janeiro", "Fevereiro", "Marco", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
tempAno = []

i = 0
for i in range(12):
	print("\n"+meses[i])
	mesesAno = int(input("Mes %d" % (i + 1) + ": "))
	tempAno.append(mesesAno)
	i += 1

somaTemp = 0
i = 0
for i in range(len(tempAno)):
	somaTemp += tempAno[i]
	i += 1

mediaTemp = somaTemp / len(tempAno)

print("Media anual da temperatura: %d graus." % mediaTemp)
print("Meses com temperatura acima da media:")

soma = 0
i = 0
for i in range(len(tempAno)):
	if tempAno[i] > mediaTemp:
		print("%s  %d graus." % (meses[i], tempAno[i]))
		soma += 1
	i += 1

if soma == 0:
	print("Nenhum mes teve temperatura acima da media.")

print("=========================================================")