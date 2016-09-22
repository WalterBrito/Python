# -*- coding: utf-8 -*-

"""
Faça um programa que calcule o valor total investido por um colecionador em sua
coleção de CDs e o valor médio gasto em cada um deles. O usuário deverá
informar a quantidade de CDs e o valor para em cada um.
"""

print("===============================================================")

quantCD = int(input("Digite a quantidade de CDs: "))

i = 0
soma = 0

while i < quantCD:
	valorCD = float(input("Digite o valor do CD: "))
	soma += valorCD
	i += 1

valorTotal = soma + quantCD
valorMedio = valorTotal / valorCD

print("O valor total gasto: %.2f" % valorTotal)
print("O valor medio gasto por cada cd foi de %.2f reais." % valorMedio)


print("===============================================================")
