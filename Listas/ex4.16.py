# -*- coding: utf-8 -*-

"""
Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus
vendedores com base em comissões. O vendedor recebe $200 por semana mais 9
por cento de suas vendas brutas daquela semana. Por exemplo, um vendedor que
teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de
$3000, ou seja, um total de $470. Escreva um programa (usando um array de
contadores) que determine quantos vendedores receberam salários nos seguintes
intervalos de valores:
a.$200 - $299
b.$300 - $399
c.$400 - $499
d.$500 - $599
e.$600 - $699
f.$700 - $799
g.$800 - $899
h.$900 - $999
i.$1000 em diante
Desafio: Crie ma fórmula para chegar na posição da lista a partir do
salário, sem fazer vários ''ifs'' aninhados.
"""

print("======================================================")

faixas = {}
faixas[(200,299)] = 0
faixas[(300,399)] = 0
faixas[(400,499)] = 0
faixas[(500,599)] = 0
faixas[(600,699)] = 0
faixas[(700,799)] = 0
faixas[(800,899)] = 0
faixas[(900,999)] = 0
faixas[(1000,10000)] = 0

vende = []
while True:
	v = float(input("Digite o total de vendas do proximo vendedor ou -1 para sair: "))
	if v == -1:
		break
	vende.append(200 + (v * 0.09))

for v in vende:
	print("vendedor: R$", v)
	for f, q in faixas.iteritems():
		if v > f[0] and v < f[1]:
			faixas[f] = q + 1
			print("Faixa Salarial: ", f)
			break

print(" 			 Relatorio Inicial         ")
print("Faixa\t\t\tQuantidade de vendedores")
for k, v in sorted(faixas.iteritems()):
	print("(%i,%i)\t\t\t%i" % (k[0], k[1], v))

print("======================================================")