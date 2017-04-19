# -*- coding: utf-8 -*-

"""
Escreva um programa que converta uma temperatura digitada em 
°C em °F. A fórmula para conversão é: F = 9 x C / 5 + 32
"""

print(60 * "=")

c = int(input("Digite um valor em °C: "))

f = ((9 * c / 5) + 32)

print("%d Celsius em Fahrenheit %.1f." % (c, f))

print(60 * "=")
