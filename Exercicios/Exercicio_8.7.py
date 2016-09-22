# -*- coding: utf-8 -*-

"""
Defina uma função que calcule o maior  divisor comum
(M.D.C) ente dois números a e b, onde a > b.

mdc(a,b) = {a 					b = 0
		   {mdc(b, a - b|a/b|) 	a > b
                        
onde a - b|a/b| pode ser escrito em python como: a  %  b.
"""

print(60 * "=")


def mdc(a, b):
    if b == 0:
        return a
    return mdc(b, a % b)

print("MDC 10 e 5 --> %d" % mdc(10, 5))
print("MDC 32 e 24 --> %d" % mdc(32, 24))
print("MDC 5 e 3 --> %d" % mdc(5, 3))

print(60 * "=")
