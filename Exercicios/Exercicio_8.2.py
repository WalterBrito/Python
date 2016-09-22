# -*- coding: utf-8 -*-

"""
Escreva uma função que receba dois números e retorne True se o 
primeiro número for múltiplo do segundo.
Valores esperados:
múltiplos(8,4) == True
múltiplos(7,3) == False
múltiplos(5,5) == True
"""


print(60 * "=")

def múltiplo(a, b):
    return a % b == 0

print("múltiplo(8,4) == True  -> resultado: %s"  % múltiplo(8, 4))
print("múltiplo(7,3) == False -> resultado: %s"  % múltiplo(7, 3))
print("múltiplo(5,5) == True  -> resultado: %s"  % múltiplo(5, 5))

print(60 * "=")
