# -*- coding: utf-8  -*-

"""
Supondo que a população de um país A seja da ordem de 80000 habitantes com
uma taxa anual de crescimento de 3%  e que a população de B seja 200000
habitantes com uma taxa de crescimento de 1.5%. Faça um programa que calcule
e escreva o número de anos necessários para que a população do país A ultrapasse
ou iguale a população do país B, mantidas as taxas de crescimento.
"""

print("===============================================================")

paisA = 80000
paisB = 200000
taxaCrescA = 0.03
taxaCrescB = 0.015

anos = 1 
while paisA < paisB:

	paisA = paisA * (1 + taxaCrescA)
	paisB = paisB * (1 + taxaCrescB)
	anos = anos + 1

print("paisA: ", round(paisA))
print("paisB: ", round(paisB))
print("Pais A ultrapassará pais B ou ira se igualar em: %d anos." % anos)
	


print("===============================================================")
