# -*- coding: utf-8 -*-

"""
Escreva um programa que verifique se um número é 
polindromo. Um número polindromo se continua o mesmo caso
seus digitos sejam invertidos.
Exemplos: 454, 10501
"""


print(60 * "=")

s = input("Digite o número sem espaços: ")
i = 0
f = len(s) - 1

while f > i and s[i] == s[f]:
    i += 1

if s[i] == s[f]:
    print("%s é polindrono" % s)
else:
    print("%s não é polindrono" % s)
print(60 * "=")
