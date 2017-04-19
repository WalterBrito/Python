# -*- coding: utf-8 -*-

"""
Escreva uma programa que leia duas strings. Verifique se a segunda
ocorre dentro da primeira e imprima a posicao de inicio.
1° string: AABBEFAATT
2° string: BE
Resultado: BE encontrado na posição 3 de AABBEFAATT
"""

print("==========================================================")

a = input("Digite o primeiro nome:")
b = input("Digite o segundo nome:")
p = a.find(b)

if p == -1:
	print("%s nao encontrada em %s." % b, a)	
else:
	print("Resultado: %s encontrado na posicao %d de %s." % (b, p, a))
	

print("==========================================================")