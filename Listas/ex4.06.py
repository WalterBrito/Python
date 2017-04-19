# -*- coding: utf-8 -*-

"""
Faça um Programa que peça as quatro notas de 10 alunos, calcule e armazene num
vetor a média de cada aluno, imprima o número de alunos com média maior ou
igual a 7.0.
"""

print("========================================================")

alunosmedia = []

for i in range(10):
	print("Nota aluno " + str(i + 1))
	media = 0
	for y in range(4):
		nota = float(input(str(y + 1) + "° nota: "))
		media += nota
	media /= 4
	alunosmedia.append(media)
for i in range(len(alunosmedia)):
	if alunosmedia[i] >= 7:
		print("Aluno %d com media %1.f" % (i + 1, alunosmedia[i]))

print("========================================================")