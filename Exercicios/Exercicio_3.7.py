# -*- coding: utf-8 -*-

"""
Escreva um programa que solicite o preço de uma mercadoria
é o percentual de desconto. Exiba o valor do desconto é o preço
preço a pagar.
"""

print(60 * "=")

mercadoria = float(input("Digite o preco da mercadoria: "))
desconto = float(input("Digite o desconto da mercadoria: "))

descMerc = (mercadoria * desconto / 100)
total = (mercadoria - descMerc)

print("Desconto: %.2f " % descMerc)
print("Total a pagar: R$ %.2f" % total)


print(60 * "=")
