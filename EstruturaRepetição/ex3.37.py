# -*- coding: utf-8 -*-

"""
Faça um programa que receba o valor de uma dívida e mostre uma tabela com os
seguintes dados: valor da dívida, valor dos juros, quantidade de parcelas e valor
da parcela.
Os juros e a quantidade de parcelas seguem a tabela abaixo:
Quantidade de Parcelas %  de Juros sobre o valor inicial da dívida
1  0
3  10
6  15
9  20
12 25
Exemplo de saída do programa:
Valor da Dívida Valor dos Juros Quantidade de Parcelas Valor da Parcela
R$ 1.000,00		0		1		R$ 1.000,00	
R$ 1.100,00		100		3		R$   366,00
R$ 1.150,00		150		6		R$   191,67 
"""

print("======================================================")

divida = float(int(input("\nDigite o valor da divida R$: ")))
juros = 0.00
print("Valor da divida: R$ %.2f" % divida)
print("Valor dos juros: %.2f" % (juros * 100))
print("Quantidade de parcelamentos: %d" % 1)
print("\nValor da parcela: R$ %.2f" % divida)

i = 3
while i < 13:
	juros += 0.5
	print("Valor da divida: R$ %.2f" % divida)
	print("Valor dos juros: %.2f" % (juros * 100))
	print("Quantidade de parcelamentos: %d" % i)
	print("\nValor da parcela: R$ %.2f" % ((divida / i) + (divida / i) * juros))
	i += 3
	
print("======================================================")
