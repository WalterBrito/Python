# -*- coding: utf-8 -*-

"""
A lista de temperaturas de Mons, na Bélgica, foi armazenada na lista
T = [-10, -8, 0, 1, 2, 5, -2, -4]. Faça um programa que imprima a menor
e a maior temperatura, assim como a temperatura média.
"""

print(60 * "=")

temp = [-10, -8, 0, 1, 2, 5, -2, -4]

maior = temp[0]
menor = temp[0]
soma = 0


for i in temp:

    if i > maior:
        maior = i
    elif i < menor:
        menor = i
    soma += i
    média = (soma / len(temp))

print("Maior temperatura: %d °C" % maior)
print("Menor temperatura: %d °C" % menor)
print("Temperatura média: %d °C" % média)

print(60 * "=")
