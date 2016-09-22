# -*- coding: UTF-8 -*-

'''
Faça um Programa que peça 2 números inteiros e um número real. 
Calcule e mostre:
a. o produto do dobro do primeiro com metade do segundo .
b. a soma do triplo do primeiro com o terceiro.
c. o terceiro elevado ao cubo.
'''

print("============================================================")

num1 = int(input("Digite o primeiro numero (int): "))
num2 = int(input("Digite o segundo numero (int): "))
num3 = int(input("Digite o terceiro numero (real): "))

a = (num1 * 2 * (num2 / 2))
b = (num1 * 3 + num3)
c = (num3 ** 3)

print("O produto do dobro do primeiro com metade do segundo e: ", a)
print("A soma do triplo do primeiro com o terceiro e: ", b)
print("O terceiro elevado ao cubo e: ", c)


print("============================================================")
