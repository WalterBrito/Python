# -*- coding:  utf-8 -*-

"""
Os números primos possuem várias aplicações dentro da Computação, por
exemplo na Criptografia. Um número primo é aquele que é divisível apenas por
um e por ele mesmo. Faça um programa que peça um número inteiro e determine
se ele é ou não um número primo.
"""

print("=======================================================")

num = int(input("Digite um numero: "))

i = 2

while i < num:
	if num % i == 0:
		a = 0
		i = num
	else:
		i += 1
		a = 1
if a == 1 or num == 2:
	print("O numero %d e primo!" % num)
else:
	print("O numero %d nao e primo." % num)

print("=======================================================")
