# -*- coding: utf-8 -*-

"""
Faça um programa que carregue uma lista com os modelos de cinco carros
(exemplo de modelos: FUSCA, GOL, VECTRA etc). Carregue uma outra lista
com o consumo desses carros, isto é, quantos quilômetros cada um desses carros
faz com um litro de combustível. Calcule e mostre:

a. O modelo do carro mais econômico;
b. Quantos litros de combustível cada um dos carros cadastrados
consome para percorrer uma distância de 1000 quilômetros e quanto isto
custará, considerando um que a gasolina custe R$ 2,25 o litro.
Abaixo segue uma tela de exemplo. O disposição das informações deve
ser o mais próxima possível ao exemplo. Os dados são fictícios e podem
mudar a cada execução do programa.

Comparativo de Consumo de Combustível:

Veículo 1
Nome: fusca
Km por litro: 7
Veículo 2
Nome: gol
Km por litro: 10
Veículo 3
Nome: uno
Km por litro: 12.5
Veículo 4
Nome: Vectra
Km por litro: 9
Veículo 5
Nome: Peugeout
Km por litro: 14.5

Relatório Final
1 - fusca	 -	7.0  - 142.0 litros - R$ 321.43 
2 - gol		 -	10.0 - 100.0 litros	- R$ 225.00
3 - uno		 -	12.5 - 80.0  litros	- R$ 180.00
4 - vectra	 -	9.0  - 111.1 litros	- R$ 250.00
5 - peugeout -	14.5 - 69.0  litros	- R$ 155.17
O menor consumo é do peugeout.
"""

print("======================================================")

modelos = {}
modmenor = 0
for i in range(5):
	modelo = input("Qual o modelo do carro?: ")
	consumo = float(input("Digite o consumo: "))
	if modmenor == 0 or consumo < modelos[modmenor]:
		modmenor = modelo
	modelos[modelo] = consumo

print()
print("---Comparativo de consumo de combustivel---")
print("----------------------------------------------")
i = 0
for m in modelos.iterkeys():
	print("Veiculo ",i,": ", m)
	print("Km por litro: ", modelos[m])
	print("------------------------------------------")
	i += 1
i = 0
print()
print("--Relatorio Final--")
print("----------------------")
for m in modelos.iterkeys():
	print(i,"- ",m," - ",modelos[m], " - ",(float(1000/modelos[m]))," litros - R$ ", (float(1000/modelos[m])*2.25))
	print("Km por litro: ", modelos[m])
	print("-----------------------------------------")
	i += 1
print("O menor consumo e do ",modmenor,".")

print("======================================================")