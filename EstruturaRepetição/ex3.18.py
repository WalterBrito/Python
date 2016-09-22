# -*- coding: utf-8 -*-

"""
Altere o programa de cálculo dos números primos, informando, caso o número
não seja primo, por quais número ele é divisível.
"""

print("===============================================================")

num = int(input("Digite um numero: "))
i = 2

while i < num:
	if num % i == 0:
		a = i
		b = 0
		i = num
	else:
		i += 1
		b = 1
if b == 1 or num == 2:
	print("Numero %d e primo!" % num)
else:
	print("Numero nao e primo, pois e divisivel por %d" % a)
	

print("===============================================================")

