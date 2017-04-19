# -*- coding: utf-8 -*-

"""
Faça um programa que peça para n pessoas a sua idade, ao final o programa
devera verificar se a média de idade da turma varia entre 0 e 25,26 e 60 e maior
que 60; e então, dizer se a turma é jovem, adulta ou idosa, conforme a média
calculada.
"""

print("===============================================================")

n = int(input("Digite o  numero de idades: "))

i = 0
soma = 0

while i < n:
	idade = int(input("Digite uma idade: "))
	soma = soma + idade
	i += 1

media = soma / i
print("Media: %d anos" % media)
if media > 0 and media <= 26:
	print("Turma Jovem!")
elif media > 26 and media <= 60:
	print("Turma Adulta.")
elif media > 60:
	print("Turma Idosa.")


print("===============================================================")
