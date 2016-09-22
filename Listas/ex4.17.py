# -*- coding: utf-8 -*-

"""
Em uma competição de salto em distância cada atleta tem direito a cinco saltos.
O resultado do atleta será determinado pela média dos cinco valores restantes.
Você deve fazer um programa que receba o nome e as cinco distâncias alcançadas
pelo atleta em seus saltos e depois informe o nome, os saltos e a média dos saltos.
O programa deve ser encerrado quando não for informado o nome do atleta. A
saída do programa deve ser conforme o exemplo abaixo:
Atleta: Rodrigo Curvêllo

Primeiro Salto: 6.5 m
Segundo Salto: 6.1 m
Terceiro Salto: 6.2 m
Quarto Salto: 5.4 m
Quinto Salto: 5.3 m

Resultado final:
Atleta: Rodrigo Curvêllo
Saltos: 6.5 - 6.1 - 6.2 - 5.4 - 5.3
Média dos saltos: 5.9 m
"""

print("=====================================================")

saltos = []

nome = input("Digite o nome do(a) atleta: ")
for i in range(5):
	saltos.append(float(input("Digite a distancia do salto: ")))

print("Atleta: ", nome)

print("Primeiro Salto: ", saltos[0], "m")
print("Segundo Salto: ",  saltos[1], "m")
print("Terceiro Salto: ", saltos[2], "m")
print("Quarto Salto: ",   saltos[3], "m")
print("Quinto Salto: ",   saltos[4], "m")

print("Resultado final:")
print("Atleta: ", nome)
str1 = "saltos: "
soma = 0

for i in range(5):
	str1 +=  " " + str(saltos[i]) + " -"
	soma += saltos[i]
str1 = str1[:-1]
soma /= 5
print(str1)
print("Media dos saltos: ", soma, " m")

print("=====================================================")