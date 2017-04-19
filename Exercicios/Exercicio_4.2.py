# -*- coding: utf-8 -*-

"""
Escreva um programa que leia três números e que imprima
o maior é o menor deles.
"""
print(60 * "=")

n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
n3 = int(input("Digite o terceiro número: "))


if n1 > n2 and n1 > n3:
    print("%d é o maior" % n1)
if n2 > n1 and n2 > n3:
    print("%d é o maior." % n2)
if n3 > n1 and n3 > n2:
    print("%d é o maior." % n3)
if n1 < n2 and n1 < n3:
    print("%d é o menor" % n1)
if n2 < n1 and n2 < n3:
    print("%d é o menor." % n2)
if n3 < n1 and n3 < n2:
    print("%d é o menor." % n3)

print(60 * "=")
