# -*- coding: utf-8 -*-

"""
Escreva  um programa que leia dois números e que pergunte qual
operação você deseja realizar. Você deve poder calcular a soma
(+), subtração (-), multiplicação (*) e divisão (/). Exiba o
resultado da operação solicitada.
"""

print(60 * "=")

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))


operação = input("Qual operação você deseja realizar? (+, -, *, /): ")

if operação == '+':
    resultado = n1 + n2
elif operação == '-':
    resultado = n1 - n2
elif operação == '*':
    resultado = n1 * n2
elif operação == '/':
    resultado = n1 / n2
else:
    print("Operação Inválida!")
    resultado = 0

print("Resultado: %d" % resultado)

print(60 * "=")
