# -*- coding: utf-8 -*-

"""
Esceva um programa que leia dois números. Imprima a divisão inteira
do primeiro pelo segundo, assim como o resto da divisão. Utilize 
apenas os operadores de soma e subtração para calcular o resultado. 
Lembre-se de que podemos entender o quociente da divisão de dois números
como a quantidade  de vezes que podemos retirar o divisor do dividendo.
Logo, 20 / 4 = 5, uma vez que podemos subtrair 4 vezes de 20.
"""

print(60 * "=")

n1 = int(input("Digite o 1° número: "))
n2 = int(input("Digite o 2° número: "))

x = n1
result = 0

while x >= n2:
	x -= n2
	result += 1
resto = x
print("%d / %d = %d" % (n1, n2, result))

print(60 * "=")
