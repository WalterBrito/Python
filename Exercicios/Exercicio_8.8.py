# -*- coding: utf-8 -*-

"""
Usando a função mdc definida no exercicio anterior, defina uma 
função para calcular o menor múltiplo comum (M.M.C) entre dois 
números.

mmc(a,b) = { |a x b| / mdc(a,b)

onde |a x b| pode ser escrito em python como: abs(a*b)
"""

print(60 * "=")

def mdc(a, b):
    if b == 0:
        return a
    return mdc(b, a % b)

def mmc(a, b):
	return abs(a * b) / mdc(a, b)

print("MDC 10 e 5 --> %d" % mmc(10, 5))
print("MDC 32 e 24 --> %d" % mmc(32, 24))
print("MDC 5 e 3 --> %d" % mmc(5, 3))

print(60 * "=")