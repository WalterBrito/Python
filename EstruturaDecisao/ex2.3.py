# -*- coding: utf-8 -*-

"""
Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a
letra escrever: F - Feminino, M - Masculino, Sexo Inválido.
"""

print("=====================================================")

sexo = input("Digite uma letra (F - Feminino, M - Masculino): ")

if sexo == "F" or sexo == "f":
	print("Letra digitada F - Feminino.")
elif sexo == "M" or sexo == "m":
	print("Letra digitada M - Masculino.")
else:
	print("Sexo invalido.")

print("=====================================================")
