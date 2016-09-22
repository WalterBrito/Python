# -*- coding: utf-8 -*-

"""
Escreva um programa que leia dois números. Imprima o resultado
da multiplicação do primeiro pelo segundo. Utilize apenas os 
operadores de soma e subtração para calcular o resultado. 
Lembre-se que podemos entender a multiplicação de dois números
como somas sucessivas de um deles. Assim, 4 x 5 = 5 + 5 + 5 + 5
= 4 + 4 + 4 + 4 + 4.
"""


print(60 * "=")

n1 = int(input("Digite o 1° número: "))
n2 = int(input("Digite o 2° número: "))

x = 1
result = 0

while x <= n2:
    result += n1
    x += 1
print("%d x %d = %d" % (n1, n2, result))

print(60 * "=")
