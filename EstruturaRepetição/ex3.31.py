# -*- coding: utf-8 -*-

"""
Encontrar números primos é uma tarefa difícil. Faça um programa que gera uma
lista dos números primos existentes entre 1 e um número inteiro informado pelo
usuário.
"""

print("========================================================")

num = int(input("Digite um numero: "))
print(1)
print(2)
print(3)
testePrimo = 5

while testePrimo < num:
	i = 2
	v = 0

	while i < testePrimo:
		resto = testePrimo % i
		if resto == 0:
			i = testePrimo
			v = 0
		if resto != 0:
			i += 1
			v = 1
	if v == 1:
		print(i)
	testePrimo += 1

print("========================================================")
