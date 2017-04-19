# -*- coding: utf-8 -*-

# Pesquisa Sequencial


print(60 * "=")

l = [15, 7, 27, 39]

p = int(input("Digite o valor a procurar: "))
x = 0

while x < len(l):
	if l[x] == p:
		break 
	x += 1

if x < len(l):
	print("%d achado na posição%d" % (p,x))
else:
	print("%d não encontrado." % p)

print(60 * "=")