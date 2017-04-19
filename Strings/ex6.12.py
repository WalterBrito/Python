# -*- coding: utf-8 -*-

"""
Escreva um programa que leia tres strings. Imprima o resultado da
substituicao na primeira, dos caracteres da segunda pelos da terceira. 
1° string: AATTGGAA
2° string: TG
3° string: Ac
Resultado: AAAACCAA
"""

print("==========================================================")

a = input("Digite o primeiro nome: ")
b = input("Digite o segundo nome: ")
c = input("Digite o terceiro nome: ")

if len(b) == len(c):
	resultado = ""
	for letra in a:
		posicao =  b.find(letra)
		if posicao != -1:
			resultado += c[posicao]
		else:
			resultado += letra
			
	if resultado == "":
		print("Todos os caracteres foram removidos.")
	else:
		print("Os caracteres %s foram removidos por %s em %s, gerando: %s." % (b, c, a, resultado))
else:
	print("Erro: A string b e c devem ter o mesmo tamanho.")

print("==========================================================")
