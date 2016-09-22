# -*- coding: utf-8 -*-

"""
Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho
em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é
de 1 litro para cada 3 metros quadrados e que a tinta é vendida em latas de 18
litros, que custam R$ 80,00. Informe ao usuário a quantidades de latas de tinta a
serem compradas e o preço total.
"""

print("=======================================================")

areaMetros = int(input("Qual o tamanho da area a ser pintada? (Metro): "))
litros =  areaMetros / 3

precoLata = 80.00
capacidadeLata = 18  # 1 lata possui 18 litros


latasTinta = litros / capacidadeLata
precoTotal = latasTinta * precoLata

print("Quantidade de latas a serem compradas: %d" % (latasTinta))
print("Preco total: R$ %.2f" % precoTotal)

print("=======================================================")
