# -*- coding: utf-8 -*-

"""
Faça um programa com uma função chamada somaImposto. A função possui dois
parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas
expressa em porcentagem e custo, que é o custo de um item antes do imposto. A
função “altera” o valor de custo para incluir o imposto sobre vendas.
"""

print("=========================================================")

def somaImposto(taxaImposto, custo):
	return custo + custo*(float(taxaImposto)/100)

custo = float(input("Digite o custo do produto: "))
taxaImposto = int(input("Digite a taxa (em %) de imposto: "))

print("Valor do custo R$: ", somaImposto(taxaImposto, custo))

print("=========================================================")