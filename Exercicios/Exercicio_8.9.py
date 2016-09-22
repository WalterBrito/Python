# -*- coding: utf-8 -*-

"""
Escreva a função para cálculo da sequência de fibonacci,
sem utilizar recursão.
"""

print(60 * "=")


def fibonacci(n):
    f = 1

    while n > 1:
        f *= n 
        n -= 1
    return f 

for x in range(7):
    print("fibonacci(%d) = %d" % (x, fibonacci(x)))
    
print(60 * "=")
