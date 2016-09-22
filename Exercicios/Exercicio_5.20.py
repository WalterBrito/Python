# -*- coding: utf-8 -*-

"""
Escreva um programa que calcule o resto da divisão inteira
entre dois números. utilize apenas as operações de soma e 
subtração para calcular o resultado.
"""


print(60 * "=")

dividendo = int(input("Digite o 1° número: "))
divisor  = int(input("Digite o 2° número: "))
quociente = 0
x = dividendo

while x >= divisor:
	x -= divisor
	quociente += quociente 
resto = x 
print("O resto de %d / %d é %d" % (dividendo, divisor, resto))

print(60 * "=")
