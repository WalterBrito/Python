# -*- coding: utf-8 -*-

# Pesquisa em uma lista usando for em vez de while.


print(60 * "=")

def soma(l):
	total = 0
	x = 0

	for x in range(5):
		total += l[x]
		x += 1
	return total 

l = [1, 7, 2, 9, 15]
print(soma(l))
print(soma([7,9,12,3,100,20,4]))

print(60 * "=")
