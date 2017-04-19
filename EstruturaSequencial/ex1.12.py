# -*- coding: UTF-8 -*-

"""
Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que
calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58.
"""

print("======================================================")

altura = float(input("Digite sua altura: "))

peso = ((72.7*altura) - 58)

print("Seu peso ideal e: %.1f" % peso)

print("======================================================")
