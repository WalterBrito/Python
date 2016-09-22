# -*- coding: utf-8 -*-

"""
Faça um programa que calcule o número médio de alunos por turma. Para isto,
peça a quantidade de turmas e a quantidade de alunos para cada turma. As turmas
não podem ter mais de 40 alunos.
"""

print("===============================================================")

n = int(input("Digite a quantidade de turmas: "))

i = 0
soma = 0

while i < n:
	turma = int(input("Digite a quantidade de alunos por turma: "))
	soma += turma
	i += 1

media = soma / i
print("Numero medio de alunos: %d" % media)


print("===============================================================")
