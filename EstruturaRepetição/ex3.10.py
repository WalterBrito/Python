# -*- coding: utf-8 -*-

"""
Desenvolva um gerador de tabuada, capaz de gerar a tabuada de qualquer número
inteiro entre 1 a 10. O usuário deve informar de qual numero ele deseja ver a
tabuada. A saída deve ser conforme o exemplo abaixo:
Tabuada de 5:
5 X 1 = 5
5 X 2 = 10
...
5 X 10 = 50
"""

print("================================================================")

tabuada = int(input("Qual tabuada voce deseja?: "))

num = 1
while num <= 10:
	print(tabuada, 'X', num, '=', tabuada * num)
	num += 1 

print("================================================================")
