# -*- coding: utf-8 -*-

# Faça um programa que verifique o menor número de uma lista.


print(60 * "=")

l = [8, 2, 12, 36, 48]

menor = l[0]

for i in l:
	if i < menor:
		menor = i 
print("Menor é %d" % menor)

print(60 * "=")