# -*- coding: utf-8 -*-

"""
Sua organização acaba de contratar um estagiário para trabalhar no Suporte de
Informática, com a intenção de fazer um levantamento nas sucatas encontradas
nesta área. A primeira tarefa dele é testar todos os cerca de 200 mouses que se
encontram lá, testando e anotando o estado de cada um deles, para verificar o que
se pode aproveitar deles.
Foi requisitado que você desenvolva um programa para registrar este
levantamento. O programa deverá receber um número indeterminado de
entradas, cada uma contendo:
um número de identificação do mouse o tipo de defeito:
a. necessita da esfera;
b. necessita de limpeza;
c.necessita troca do cabo ou conector;
d.quebrado ou inutilizado
Uma identificação igual a zero encerra o programa. Ao final o
programa deverá emitir o seguinte relatório:

Quantidade de mouses: 100

Situação			    	Quantidade			Percentual
1- necessita da esfera		40					40%
2- necessita de limpeza		30					30%
3- necessita troca do cabo 
ou conector 				15					15%
4- quebrado ou inutilizado	15					15%
"""

print("======================================================")

defeitos = ["necessita da esfera", "necessita de limpeza",
 "necessita troca do cabo", "conector quebrado ou inutilizado"]
somaDefeitos = [0, 0, 0, 0]

i = 1
while i != 0:
	print("1-necessita da esfera\n2-necessita de limpeza\n3-necessita troca do cabo\n4-conector quebrado ou inutilizado")
	defeito =  int(input("Digite o numero referente ao defeito do mouse ou 0 para sair: "))
	if defeito != 0:
		somaDefeitos[defeito-1] = somaDefeitos[defeito-1] + 1
	else:
		i = 0

i = 0
soma = 0
while i < len(somaDefeitos):
	soma += somaDefeitos[i]
	i += 1

print("\n\nSituacao			Quantidade		Percentual")

i = 0
while i < len(somaDefeitos):
	print((i + 1)," - "+defeitos[i]+"		", somaDefeitos[i],"		",100*(float(somaDefeitos[i] / soma)), "%")
	i += 1

print("======================================================")