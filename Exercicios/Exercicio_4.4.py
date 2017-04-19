# -*- coding: utf-8 -*-

"""
Escreva um programa que pergunte a distância que um passageiro
deseja percorrer em km. Calcule o preço da passagem, cobrando
R$ 0,50 por km para viagens de até 200 km, e R$ 0,45 para viagens
mais longas.
"""

print(60 * "=")
distânciaKm = int(input("Digite a distância a ser percorrida (Km): "))
preçoPassagem1 = distânciaKm * 0.50
preçoPassagem2 = distânciaKm * 0.45

if distânciaKm <= 200:
    print("O preço da passagem é de %.2f." % preçoPassagem1)
else:
    print("O preço da passagem é de %.2f." % preçoPassagem2)

print(60 * "=")
