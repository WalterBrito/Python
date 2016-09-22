# -*- coding: utf-8 -*- 

"""
Em uma eleição presidencial existem quatro candidatos. Os votos são informados
por meio de código. Os códigos utilizados são:
1 , 2, 3, 4 - Votos para os respectivos candidatos
(você deve montar a tabela ex: 1 - Jose/ 2- João/etc)
5 - Voto Nulo
6 - Voto em Branco
Faça um programa que calcule e mostre:
a. O total de votos para cada candidato;
b. O total de votos nulos;
c. O total de votos em branco;
d. A percentagem de votos nulos sobre o total de votos;
e. A percentagem de votos em branco sobre o total de votos.

Para finalizar o conjunto de votos tem-se o valor zero.
"""

print("========================================================")

print("Opcoes: \n(1) - Joao \n(2) - Jose \n(3) - Marcos \n(4) - Eneas \n(5) - Voto Nulo \n(6) - Voto em Branco \n(0) - Sair\n")

voto = 1
soma = 0
soma1 = 0
soma2 = 0
soma3 = 0
soma4 = 0
soma5 = 0
soma6 = 0

while voto != 0:
	voto = int(input("Digite o codigo do seu voto: "))

	if voto == 1:
		soma1 += 1
	elif voto == 2:
		soma2 += 1
	elif voto == 3:
		soma3 += 1
	elif voto == 4:
		soma4 += 1
	elif voto == 5:
		soma5 += float(1)
	elif voto == 6:
		soma6 += float(1)

	soma += 1

print("Votos para o Joao: %d" % soma1)
print("Votos para o Jose: %d" % soma2)
print("Votos para o Marcos: %d" % soma3)
print("Votos para o Eneas: %d" % soma4)
print("Percentagem Votos Nulos: %d" % ((soma5/soma)*100) + "%")
print("Percentagem Votos em Branco: %d" % ((soma6/soma)*100) + "%")

print("========================================================")
