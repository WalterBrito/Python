# -*- coding: utf-8 -*-

"""
Faça um programa que leia um número indeterminado de valores,
correspondentes a notas, encerrando a entrada de dados quando for informado um
valor igual a -1 (que não deve ser armazenado). Após esta entrada de dados, faça:
a. Mostre a quantidade de valores que foram lidos;
b. Exiba todos os valores na ordem em que foram informados, um ao
lado do outro;
c. Exiba todos os valores na ordem inversa à que foram informados,
um abaixo do outro;
d. Calcule e mostre a soma dos valores;
e. Calcule e mostre a média dos valores;
f. Calcule e mostre a quantidade de valores acima da média
calculada;
g. Calcule e mostre a quantidade de valores abaixo de sete;
h. Encerre o programa com uma mensagem;
"""

print("======================================================")

valores = []
i = 0
soma = 0

while True:
	print("Digite -1 para sair.")
	num = int(input("Numero %d" % (i + 1) + ": "))
	if num == -1: 
		break
	valores.append(num)
	
print("Quantidade de valores: ", len(valores))

print("Numeros informados: ", valores)	

print("Numeros na ordem inversa: ")
for i in reversed(valores):	
	print(i)

print("Soma: ")
for i in valores:
	soma += i
print(soma)
	
media = soma / len(valores)
print("Media: ", media)

print("Quantidade acima da media: ")
quantAcimaMedia = 0
for i in valores:
	if i > media: 
		quantAcimaMedia += 1
print(quantAcimaMedia)
		
print("Quantidade abaixo da sete: ")
quantAbaixo7 = 0
for i in valores:
	if i < 7: 
		quantAbaixo7 += 1
print(quantAbaixo7)			

print("Fim")

print("======================================================")