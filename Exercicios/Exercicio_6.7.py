# -*- coding: utf-8 -*-

"""
Explique porque nem todos os while oidem ser convertidos em for.
"""

print(60 * "=")

l = []

while True:
    num = int(input("Digite um número: "))

    if num == 0:
        break
    l.append(num)

for i in l:
    print("l = [%d]" % i)

print(60 * "=")

"""
O primerio wile não pode ser convertido em for porque o número 
de repetições é desconhecido no inicio.
"""
