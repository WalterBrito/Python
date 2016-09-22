# -*- coding: utf-8 -*-

"""
Escreva um programa que pergunte a quantidade de km percorridos por 
um carro alugado pelo usuário, assim como a quantidade de dias pelos
quais os carros foram alugado. Calcule o preço a pagar, sabendo que 
o carro custa R$ 60 por dia e R$ 0,15 por km rodado.
"""

print(60 * "=")

quantKM = float(input("Digite a quantidade de km percorridos: "))
quantDias = int(input("Digite a quantidade de dias: "))

precoDia = 60
precoKm = 0.15

precoTotal = (quantKM * precoKm + quantDias * precoDia)

print("O preço á pagar R$ %.2f." % precoTotal)

print(60 * "=")
