# -*- coding: UTF-8 -*-

'''
Faça um Programa que peça a temperatura em graus Farenheit, transforme e
mostre a temperatura em graus Celsius.
C = (5 * (F-32) / 9).
'''

print("========================================================")

f = float(input("Digite o valor da temperatura: "))

c = ((f - 32) * 5 / 9)

print("Conversao °F para °C e: %.1f" % c)

print("========================================================")
