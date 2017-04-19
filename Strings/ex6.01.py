# -*- coding: utf-8 -*-

"""
'''Tamanho de strings.''' Faça um programa que leia 2 strings e informe o conteúdo
delas seguido do seu comprimento. Informe também se as duas strings possuem o
mesmo comprimento e são iguais ou diferentes no conteúdo.

Compara duas strings
String 1: Brasil Hexa 2006
String 2: Brasil! Hexa 2006!
Tamanho de "Brasil Hexa 2006": 16 caracteres
Tamanho de "Brasil! Hexa 2006!": 18 caracteres
As duas strings são de tamanhos diferentes.
As duas strings possuem conteúdo diferente.
"""

print("=========================================================")

string1 = input("Digite a primeira string: ").capitalize()
string2 = input("Digite a segunda string: ").capitalize()

numString1 = len(string1)
numString2 = len(string2)

print("\nComparando as strings")
print("string1: " + string1)
print("string2: " + string2)
print("Tamanho de %s e de %s caracteres. " % (string1, numString1))
print("Tamanho de %s e de %s caracteres. " % (string2, numString2))

if numString1 != numString2:
	print("As duas strings sao de tamanhos diferentes.\nAs duas strings possuem palavras diferentes.")
elif string1 == string2:
	print("As duas strings sao iguais.")

print("=========================================================")